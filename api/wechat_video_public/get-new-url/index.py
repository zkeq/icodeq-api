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


def get_new_url(wxv, num=0):
    url = f'https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz=&mid=&idx=&vid={wxv}&uin=&key=&pass_ticket=&wxtoken=&appmsg_token=&x5=0&f=json'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    wxv_content = requests.get(url, headers=headers).json()
    try:
        url_content = wxv_content["url_info"][num]['url']
    except KeyError and IndexError as e:
        print(e)
        return 0
    url_content = url_content.replace('http://', 'https://')
    r.set(wxv, url_content, ex=9000)
    return url_content


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_new_url(wxv=self.path.split('?')[1])
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return None
