from flask import Flask, render_template, request, escape
from get_results import All_Results
import helper


app = Flask(__name__)

#Submit Filter Form
@app.route("/", methods=["GET"])
def action_html_form():
    if request.method == 'GET':
        # start Get Data
        Helper = helper.Helper(request.args, escape)
        gsApiKey = Helper.get_api_key()
        gsOtherPram = Helper.query_string()
        searchResults = Helper.httpRequest('search', gsApiKey, gsOtherPram)
        searchResults = searchResults.get('organic')
        
        return render_template(
            'index.html',
            apiKey=gsApiKey,
            requestArgs=request.args,
            searchResults=searchResults,
            results=All_Results(),
            
        )
    else:
        return render_template('index.html')


#App Run
if __name__ == "__main__":
    app.run()
