#coding=utf-8
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os,re

def headers(referer):
    headers = {
        'Host': 'http://www.js518.net/lianaishenghuo/5859/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                       ' Chrome/77.0.3865.120 Safari/537.36',
        'Referer': '{0}'.format(referer)
    }
    return headers

def img_headers(referer):
    headers = {
        'Host': 'j.aiwenwo.net',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/77.0.3865.120 Safari/537.36',
        'Referer': '{0}'.format(referer)
    }
    return headers

def each_chapter():
    url = 'http://www.js518.net/lianaishenghuo/5859/'
    res = requests.get(url, headers(url))
    res.encoding = 'utf-8'
    sel = BeautifulSoup(res.text, 'lxml')
    total_html = sel.find('ol', id='mh-chapter-list-ol-0')
    total_chapter = []
    for i in total_html.find_all('li'):
        href = i.a['href']
        every_url = 'http://www.js518.net/'+href
        total_title = i.get_text()
        try:
            a = re.findall(r"\d", total_title)
            b = ''.join(a)
            if int(b) == 1:
                total_chapter.append(every_url)
                try:
                    name = u"{}".format(total_title)
                    name.split()
                    os.mkdir(name[:-1])
                except Exception as e:
                    print(e)
            else:
                pass
        except Exception as e:
            print(e)
    return total_chapter

def each_page(url):
    every_page_url = '{}'.format(url)
    html = main(every_page_url)
    soups = BeautifulSoup(html, 'lxml')
    try:
        soup = soups.find('select', id='k_pageSelect')
        pages = soup.find_all('option')
    finally:
        pass
    return len(pages)

def get_image(whole_url,page):
    try:
        html = main(whole_url)
        soups = BeautifulSoup(html, 'lxml')
        soup = soups.find('img', id='qTcms_pic')
        src = soup['src']
        alt1 = str(soup['alt'])
        title = alt1[6:-10]
        f_name = u'%s/ %s/第%s页.jpg' % (os.path.abspath('.'), title, page)
        with open(f_name, "wb+") as jpg:
            r = requests.get(src, headers=img_headers(src))
            jpg.write(r.content)
            download = u'已下载%s第%s页' % (title, page)
            print(download)
    except Exception as e:
        print(e)

def main(whole_url):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    bro = webdriver.Chrome(chrome_options=chrome_options)
    bro.get(whole_url)
    html = bro.page_source
    return html


if __name__ == '__main__':
    for i in each_chapter():
        each_pages = each_page(i)
        for j in range(1, each_pages+1):
            page = j
            whole_url = i + '?p=' + str(j)
            get_image(whole_url, page)
