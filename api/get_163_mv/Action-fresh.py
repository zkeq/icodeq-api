# coding:utf-8

from selenium import webdriver
import redis
from lxml import etree
from urllib.parse import unquote
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password="7d6531a1d3694184ab459e84b587bc53", ssl=True)


def get_video_url(id):
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
    browser.get("https://music.163.com/#/mv?id={0}".format(id))
    browser.switch_to.frame("contentFrame")
    source = browser.page_source
    html = etree.HTML(source)
    video_all = html.xpath('//*[@id="flash_box"]/@data-flashvars')
    try:
        video_all = video_all[0].split('&')[0].split('=')[1]
    except IndexError:
        video_all = ''
    _video_url = unquote(video_all).replace('http://', 'https://')
    browser.quit()
    return _video_url


def post_mv_2_redis(_video_id, _video_url):
    r.set(_video_id, _video_url, ex=9000)
    return_url = r.get(_video_id)
    return return_url


if __name__ == '__main__':
    video_list = ['14401004', '14424820']
    # video_url = r.get('163_mv_' + video_id)
    # if not video_url:
    for video_id in video_list:
        video_url = get_video_url(video_id)
        post_mv_2_redis('163_mv_' + video_id, video_url)
        print(video_url)
    print('执行完毕！')