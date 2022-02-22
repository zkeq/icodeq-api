# coding:utf-8
import redis
import time
import requests
from http.server import BaseHTTPRequestHandler


r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port='32369',
    password='9a4bbcdc0b88484ab13ec54098ea5fb0', ssl=True)


# 获取当前时间戳
def get_time_stamp():
    return int(time.time())


# 查看当前时间是否大于45分钟
def check_time():
    if r.get('time') is None:
        r.set('time', get_time_stamp(), ex=2700)
        return False
    else:
        return True


def get_video():
    if check_time():
        _video_url = r.get('video')
        return _video_url.decode('utf-8')
    else:
        url = 'https://api.icodeq.com/api/weibo_307_video/get-new-url'
        _video_url = requests.get(url).text
        r.set('video', _video_url, ex=3600)
        return _video_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = get_video()
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return None
