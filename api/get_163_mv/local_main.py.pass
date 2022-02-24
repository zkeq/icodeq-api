# coding:utf-8
# 本文件已迁移至 Github Actions. 
# 详情 Action-fresh.py

from selenium import webdriver
import redis
from lxml import etree
import os
from urllib.parse import unquote

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password='7d6531a1d3694184ab459e84b587bc53', ssl=True)


def get_video_url(id):
    driver = webdriver.Chrome(options=chrome_options)  # executable_path=chromedriver
    driver.get("https://music.163.com/#/mv?id={0}".format(id))
    driver.switch_to.frame("contentFrame")
    source = driver.page_source
    html = etree.HTML(source)
    print(source)
    video_all = html.xpath('//*[@id="flash_box"]/@data-flashvars')
    try:
        video_all = video_all[0].split('&')[0].split('=')[1]
    except IndexError:
        video_all = ''
    _video_url = unquote(video_all)
    driver.quit()
    return _video_url


def post_mv_2_redis(_video_id, _video_url):
    r.set(_video_id, _video_url)
    return_url = r.get(_video_id)
    return return_url


if __name__ == '__main__':
    video_id = '14401004'
    video_url = get_video_url(video_id)
    # post_mv_2_redis('163_mv_' + video_id, video_url)
    print(video_url)