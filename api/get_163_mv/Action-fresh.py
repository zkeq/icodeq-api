# coding:utf-8

from selenium import webdriver
import redis
from lxml import etree
from urllib.parse import unquote
from selenium.webdriver.chrome.options import Options
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video_url(_id):
    browser = webdriver.Chrome('/usr/bin/chromedriver', options=chrome_options)
    browser.get("https://music.163.com/#/mv?id={0}".format(_id))
    browser.switch_to.frame("contentFrame")
    source = browser.page_source
    html = etree.HTML(source)
    video_all = html.xpath('//*[@id="flash_box"]/@data-flashvars')
    print("获取到的数据为: ", video_all)
    print('-' * 100)

    try:
        video_all = video_all[0].split('&')[0].split('=')[1]
    except IndexError:
        video_all = ''
    _video_url = unquote(video_all).replace('http://', 'https://')
    browser.quit()
    return _video_url


def post_mv_2_redis(_video_id, _video_url):
    print('正在将获取到的视频地址放入 Redis 中: ', end=' ')
    print(r.set(_video_id, _video_url, ex=6000))
    return_url = r.get(_video_id)
    return return_url


if __name__ == '__main__':
    video_list = ['14401004', '14351340']
    # video_url = r.get('163_mv_' + video_id)
    # if not video_url:
    for video_id in video_list:
        video_url = get_video_url(video_id)
        print("正在获取 ID: {} 所对应链接: ".format(video_id), video_url)
        post_mv_2_redis('163_mv_' + video_id, video_url)
        print('-' * 100)
    print('执行完毕！')
