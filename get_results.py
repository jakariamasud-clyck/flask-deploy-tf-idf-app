from flask import request, escape
from get_sentences import Sentences
import helper
import tfidf


class All_Results:
    # Result By Url
    def get_results(self, url, getType=False):
        sentences = Sentences()
        tfIdf = tfidf.TfIdf()
        get_sentences = sentences.get_sentences(url)
        if(not get_sentences):
            return
        sentences = tfIdf._sentences(get_sentences)
            
        total_documents = tfIdf._total_documents(sentences)

        freq_matrix = tfIdf._create_frequency_matrix(sentences)
        tf_matrix = tfIdf._create_tf_matrix(freq_matrix)
        count_doc_per_words = tfIdf._create_documents_per_words(freq_matrix)
        idf_matrix = tfIdf._create_idf_matrix(freq_matrix, count_doc_per_words, total_documents)
        tf_idf_matrix = tfIdf._create_tf_idf_matrix(tf_matrix, idf_matrix)
        sentence_scores = tfIdf._score_sentences(tf_idf_matrix)
        threshold = tfIdf._find_average_score(sentence_scores)
        summary = tfIdf._generate_summary(sentences, sentence_scores, 1.3 * threshold)
        
        results = {}

        for tfs in tf_matrix:
            if(tf_matrix[tfs]):
                for tfKey, tfVal in tf_matrix[tfs].items():
                    if(tfKey.isalpha()):
                        results[tfKey] = {'tf': round(tfVal, 2), 'avrg_scr': round(threshold, 2)}

        results = tfIdf._results_update(tf_idf_matrix, 'tfidf', results)
        otherScores = {
            'sentence_scores' : sentence_scores,
            'summary': summary,
        }
        if(getType in otherScores):
            return otherScores.get(getType)
        if(getType == 'all'):
            results = tfIdf._results_update(freq_matrix, 'freq', results)
            results = tfIdf._results_update(idf_matrix, 'idf', results)

        return results

    # Get All Texts
    def get_all_texts(self):
        sentences = Sentences()
        Helper = helper.Helper(request.args, escape)
        gsApiKey = Helper.get_api_key()
        gsOtherPram = Helper.query_string()
        searchResults = Helper.httpRequest('search', gsApiKey, gsOtherPram)
        searchResults = searchResults.get('organic')
        getAllText = ''
        for sVal in searchResults:
            if(sVal.get('url')):
                get_sentences = sentences.get_sentences(sVal.get('url'))
                getAllText = getAllText + get_sentences
                    
        return getAllText
    
    # Get All Results
    def get_all_results(self):
        Helper = helper.Helper(request.args, escape)
        gsApiKey = Helper.get_api_key()
        gsOtherPram = Helper.query_string()
        searchResults = Helper.httpRequest('search', gsApiKey, gsOtherPram)
        searchResults = searchResults.get('organic')
        setRlt = {}
        for sVal in searchResults:
            if(sVal.get('url')):
                get_results = self.get_results(sVal.get('url'), 'all')
                if(get_results):
                    for k, v in get_results.items():
                        if(k in setRlt.keys()):
                            setRlt[k].update({
                                'tf': round(setRlt[k]['tf'] + v['tf'], 2),
                                'avrg_scr': round(setRlt[k]['avrg_scr'] + v['avrg_scr'], 2),
                                'tfidf': round(setRlt[k]['tfidf'] + v['tfidf'], 2),
                                'freq': round(setRlt[k]['freq'] + v['freq'], 2),
                                'idf': round(setRlt[k]['idf'] + v['idf'], 2),
                            })
                        else:
                            setRlt[k] = v
                        
        return setRlt
