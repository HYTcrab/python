# 一个HTML文件，找出里面的正文。
import bs4
import requests
import re

def process():
    url='https://www.douban.com/'
    r=requests.get(url)
    html=r.text
    soup = bs4.BeautifulSoup(html, 'html.parser')
    [script.extract() for script in soup.find_all('script')]
    [style.extract() for style in soup.find_all('style')]
    soup.prettify()
    #reg1 = re.compile("<[^>]*>")
    #content = reg1.sub('', soup.prettify())
    content=soup.get_text(strip=True)
    contents=[t for t in content.split()]
    print(contents)
if __name__=="__main__":
    process()