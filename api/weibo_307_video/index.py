# coding:utf-8
import redis
from http.server import BaseHTTPRequestHandler
import os
import time
import requests


env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


def get_video(cursor, url_data, hd):
    _video_url = r.get('weibo_{}_'.format(hd) + cursor)
    if _video_url is None:
        url = 'https://api.icodeq.com/api/weibo_307_video/get-new-url?{data}'.format(data=url_data)
        _video_url = requests.get(url).text
    else:
        _video_url = _video_url.decode('utf-8')
    while _video_url is None:
        _video_url = r.get('weibo_' + cursor).decode('utf-8')
        time.sleep(0.5)
        print('waiting for video url')
    return _video_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_data = self.path.split('?')[1]
        cursor = url_data.split('&')[1].split('=')[1]
        hd = int(url_data.split('&')[2].split('=')[1])
        url = get_video(cursor, url_data, hd)
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=2700')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return None
