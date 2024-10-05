import requests
import urllib.request
import time
from bs4 import BeautifulSoup

def main():
    url = 'http://web.mta.info/developers/turnstile.html'
    response = requests.get(url)
    # print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")
    # for line in soup.findAll('a'):
    #     print(line)

    one_a_tag = soup.findAll('a')[38]
    link = one_a_tag['href']
    print(link)
    download_url = 'http://web.mta.info/developers/'+ link
    urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
    time.sleep(1)
if __name__ == "__main__":
    main()