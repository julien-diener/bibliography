"""
Read google scholar (registered) user citation 
"""

from urllib import FancyURLopener
import re

try:
    from bs4 import SoupStrainer, BeautifulSoup
    BS_VERSION = 4
except ImportError:
    from BeautifulSoup import SoupStrainer, BeautifulSoup
    BS_VERSION = 3


class MyOpener(FancyURLopener):
    version = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'


class Query(object):
    sorry_filter= '<title>.*Sorry.*</title>'
    name_filter = '<title>(.*)-.*</title>'
    pub_filter  = ['tr',{'class':'gsc_a_tr'}]
    
    def __init__(self, user_id):
        self.user_id = user_id
        self.url = "http://scholar.google.fr/citations?user="+self.user_id
        ##possible todo: &cstart=0&pagesize=20

        self.html = MyOpener().open(self.url).read()
        
        refused = len(re.findall(Query.sorry_filter,self.html))>00
        
        if refused:
            self.error = True;
        else:
            self.error = False;
            self.parse();
        

    def parse(self):
        self.username = re.findall(Query.name_filter,self.html)[0]
        
        if BS_VERSION==4:
            pubTree = BeautifulSoup(self.html, parse_only=SoupStrainer(*Query.pub_filter))
        else:
            pubTree = BeautifulSoup(self.html, parseOnlyThese=SoupStrainer(*Query.pub_filter))
        
        publication = []
        for pub in pubTree.findAll(*Query.pub_filter):
            tmp = list(pub.children.next().children)
            p = {}
            if len(tmp)>0: 
                p['title'] = tmp[0].string
                p['href']  = "http://scholar.google.fr/" + tmp[0].get('href')
            if len(tmp)>1: 
                p['authors'] = tmp[1].string
            if len(tmp)>2:
                tmp2 = list(tmp[2].children)
                if len(tmp2)>0: p['journal'] = tmp2[0]
                if len(tmp2)>1: p['year']    = tmp2[1].string.strip(' ,')
            publication.append(p)
        
        self.publication = publication
        
    def __repr__(self):
        return repr(self.publication)
    
