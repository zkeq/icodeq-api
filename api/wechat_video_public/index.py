# coding:utf-8
import time

import redis
from http.server import BaseHTTPRequestHandler
import os
import requests

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video(wxv):
    _video_url = r.get(wxv)
    if _video_url is None:
        url = 'https://api.icodeq.com/api/wechat_video_public/get-new-url?{wxv}'.format(wxv=wxv)
        requests.get(url)
    while _video_url is None:
        video_url = r.get(wxv)
        time.sleep(0.7)
    return _video_url.decode('utf-8')


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = get_video(wxv=self.path.split('?')[1])
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return None