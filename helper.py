import requests
import urllib.parse

# Start Helper Class
class Helper:
    # init
    def __init__(self, rq, escape):
        

        self.parse = urllib.parse
        self.rq = rq
        self.escape = escape

    # httpRequest
    def get_api_key(self):
        return '9cbfb3c0-fdc8-11eb-865b-5b6962f86cb2'

    # httpRequest
    def httpRequest(self, endPoint, apiKey, otherPram='', rqType='GET', datas={}):
        if(not endPoint):
            return
        self.endPoint = f"https://app.zenserp.com/api/v2/{endPoint}?"
        self.otherPram = f"&{otherPram}" if otherPram else ""
        self.apiKey = apiKey if apiKey else "9cbfb3c0-fdc8-11eb-865b-5b6962f86cb2"
        self.apiKey = f"apikey={self.apiKey}"
        rqUrl = self.endPoint + self.apiKey + self.otherPram
        if(rqType == 'POST'):
            rq = requests.post(rqUrl, datas)
        else:
            rq = requests.get(rqUrl)
        return rq.json() if rq.json() else []

    # Filter Data
    def form_filter(self, rq):
        rq = self.parse.quote(self.escape(rq)) if rq else False
        return rq

    # Get Qury Data
    def qury_data(self):
        q = 'q=intext:'+self.parse.quote(self.rq.get('q')) if self.rq.get('q') else ''
        url = self.form_filter(self.rq.get('url'))
        if(url):
            url = url.replace('https', '').replace('http', '').replace(
                'www.', '').replace('://', '').replace('/', '')
            url = url.strip()
            q = f"{q}+site:{url}"
        return q

    # Form Submition
    def query_string(self):
        queryList = [self.qury_data()]
        queryArgs = ['q', 'url', 'device', 'search_engine',
                     'gl', 'location', 'num', 'hl', 'lat', 'lng']

        if(queryArgs):
            explodeItem = ['gl', 'hl']
            skips = ['q', 'url']
            for arg in queryArgs:
                if(arg in skips):
                    continue
                if(self.rq.get(arg)):
                    getQueryStr = self.rq.get(arg)
                    if(getQueryStr and (arg in explodeItem)):
                        setArg = getQueryStr.split()[0]
                        if(setArg):
                            setArg = setArg.lower()
                            queryList.append(f"{arg}={setArg}")
                    else:
                        if(getQueryStr):
                            getQueryStr = self.form_filter(getQueryStr).lower()
                            queryList.append(f"{arg}={getQueryStr}")
                        
        return "&".join(queryList)
