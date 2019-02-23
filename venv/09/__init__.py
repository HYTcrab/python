#一个HTML文件，找出里面的链接
import bs4
import requests

def process():
    url='https://www.douban.com/'
    r=requests.get(url)
    html=r.text
    soup=bs4.BeautifulSoup(html,'html.parser')
    [script.extract() for script in soup.find_all('script')]
    [style.extract() for style in soup.find_all('style')]
    soup.prettify()
    s=soup.find_all('a')
    for i in s:
        print(i.get('href'))
if __name__=="__main__":
    process()