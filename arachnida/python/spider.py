import requests
import re

def find_links(initial_url):
    found, to_crawl = [], []
    to_crawl.append(initial_url)
    urlset=set()
    asterisk = "*"

    while to_crawl:
        current_url = to_crawl.pop(0)
        #print(current_url)
        r = requests.get(current_url)
        to_crawl.append(current_url)
        # Match between "" or "? --> "(.*?)\?|\"(.*?)\"
        # Stop regex after ? --> (\?[^;]*)
        # Ignore whitespace --> \s*?
        # Search every a tag and get only string inside quotes --> <a href="([^"]+)"> 
        for url in re.findall('<a href="([^"]+)"\s*?>', str(r.text)):
            url = url.split('?')[0].split('#')[0]
            print(asterisk + " - " + url)
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url):
                to_crawl.append(url)
                urlset.add(url)
        #print(asterisk + " - " + url)
    return to_crawl

find_links('https://mercadodevida.es')