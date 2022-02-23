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
    title = '获取微信API失败，请检查接口是否已更换'
    content = str(err_msg)
    url_full = base_url + 'title=' + title + '&desp=' + content
    url_encode = quote(url_full, safe='/:?=&%20')
    requests.get(url_encode)


def get_new_url(wxv, num=0):
    cookie = r.get('cookie')
    url = f'https://mp.weixin.qq.com/mp/videoplayer?action=get_mp_video_play_url&preview=0&__biz=&mid=&idx=&vid={wxv}&uin=&key=&pass_ticket=&wxtoken=&appmsg_token=&x5=0&f=json'
    headers = {
        'Cookie': cookie,
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'}
    wxv_content = requests.get(url, headers=headers).json()
    try:
        url_content = wxv_content["url_info"][num]['url']
    except KeyError and IndexError as e:
        send_err(e)
        return 0
    url_content = url_content.replace('http://', 'https://')
    r.set(wxv, url_content, ex=18000)
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
