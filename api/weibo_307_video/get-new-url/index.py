# coding:utf-8
import requests
import redis
from http.server import BaseHTTPRequestHandler
from urllib.parse import quote
import time
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def send_err(err_msg):
    base_url = 'https://sctapi.ftqq.com/SCT33292TX3fnGuyxnE4XZEG4CYQXE63P.send?'
    title = '获取微博API失败，请检查Cookie是否正确'
    content = str(err_msg)
    url_full = base_url + 'title=' + title + '&desp=' + content
    url_encode = quote(url_full, safe='/:?=&%20')
    requests.get(url_encode)


# 获取当前时间戳
def get_time_stamp():
    return int(time.time())


def get_new_url(uid, cursor, hd):
    cookie = r.get('cookie')
    cursor += 1
    url = f'https://weibo.com/ajax/profile/getWaterFallContent?uid={uid}&cursor={cursor}'
    print(url)
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    content = requests.get(url, headers=headers).json()
    try:
        w100w = content['data']['list'][0]['page_info']['media_info']['playback_list'][hd]['play_info']['url']
    except KeyError and IndexError as e:
        send_err(e)
        return 0
    w100w = w100w.replace('http://', 'https://')
    r.set('weibo_{}_'.format(str(hd)) + cursor, w100w, ex=3600)
    return w100w


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_data = self.path.split('?')[1]
        print('url_data:', url_data)
        cursor = int(url_data.split('&')[0].split('=')[1])
        print('cursor:', cursor)
        hd = int(url_data.split('&')[1].split('=')[1])
        print('hd:', hd)
        uid = url_data.split('&')[2].split('=')[1]
        print('uid:', uid)
        data = get_new_url(uid, cursor, hd)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return None
