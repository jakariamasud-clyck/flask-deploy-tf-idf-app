from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter
import requests

# Start TfIdf Class
class Sentences:
    
    # Tag Visible
    def tag_visible(self,element):
        if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
            return False
        if isinstance(element, Comment):
            return False
        return True

    # Text From Html
    def text_from_html(self, body):
        soup = BeautifulSoup(body, 'html.parser')
        texts = soup.findAll(text=True)
        visible_texts = filter(self.tag_visible, texts)
        return u" ".join(t.strip() for t in visible_texts)
    
    # Get Html By Url
    def get_html(self, url):
        rq = requests.get(url)
        htmltext = rq.text if rq.status_code == 200 else False
        return htmltext if htmltext else False
    # Text From Html
    def get_sentences(self, url):
        getHtml = self.get_html(url)
        return self.text_from_html(getHtml) if getHtml else False
    
    # Count BackLinks
    def count_backlinks(self,body):
        soup = BeautifulSoup(body, "html.parser")
        foundUrls = Counter([link["href"] for link in soup.find_all("a", href=lambda href: href and not href.startswith("#"))])
        foundUrls = foundUrls.most_common()
        count = 0
        for item in foundUrls:
            if(item):
                count = count+1
        return count
