from bs4 import BeautifulSoup, SoupStrainer
import urllib.request
import requests

def download_file(url):
    local_filename = url.split('/')[-2]
    local_ext = url.split('/')[-1]
    local = local_filename + local_ext
    print(local)
    r = requests.get(url, stream=True)
    with open(local, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    return local

def chips(page_number):
    url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=m570.l1313&_nkw=old+integrated+circuits&_sacat=0&LH_TitleDesc=0&_osacat=0&_odkw=vintage+integrated+circuits&_pgn=' + str(page_number)

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    imgs = soup.findAll("img")

    for img in imgs:
        print(img['src'])
        url = img['src']
        download_file(url)


for x in range(1, 6):
    chips(x)
