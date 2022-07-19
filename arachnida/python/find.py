import requests
import re
import sys
import getopt

# import web_pdb; web_pdb.set_trace()

def save_html(html, path):
    with open(path, 'a') as f:
        f.write(html)

def uniq(urlset, url):
    uri = []
    url = url.split('://')[1]
    print(url)
    for urls in range(len(urlset)):
        uri = urlset[urls]
        save_html(uri+"\n", "./"+ url +".txt")

def crawl_web(initial_url):
    crawled = []
    to_crawl = []
    to_crawl.append(initial_url)
    urlset=set()
    i=0
    j=0
    limit = 3

    while i < limit:
        current_url = to_crawl.pop(0)
        r = requests.get(current_url)
        crawled.append(current_url)
        r = requests.get(current_url)
        for url in re.findall('<a href="([^"]+)"\s*?>', str(r.text)):
            url = url.split('?')[0].split('#')[0]
            if url[0] == '/':
                url = current_url + url
            pattern = re.compile('https?')
            if pattern.match(url):
                to_crawl.append(url)
                urlset.add(url)
        i += 1
        j += 1
    uniq(list(urlset), initial_url)
    return crawled

def arguments():
    url_input = None
    level = None
    path = "./data/"
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "r:l:p:")
    except:
        print("Error")
    for opt, arg in opts:
        if opt in ['-r']:
            url_input = arg
        elif opt in ['-l']:
            level = arg
        elif opt in ['-p']:
            path = arg
    crawl_web(url_input)

arguments()
