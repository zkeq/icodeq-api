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
    print('data:', 'weibo_{}_'.format(hd) + cursor)
    print('_video_url:', _video_url)
    if _video_url is None:
        url = 'https://api.icodeq.com/api/weibo_307_video/get-new-url?{data}'.format(data=url_data)
        _video_url = requests.get(url).text
    else:
        _video_url = _video_url.decode('utf-8')
    while _video_url is None:
        time.sleep(0.5)
        _video_url = r.get('weibo_{}_'.format(hd) + cursor).decode('utf-8')
        print('waiting for video url')
    print('video url:', _video_url)
    return _video_url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url_data = self.path.split('?')[1]
        print('url_data:' + url_data)
        cursor = url_data.split('cursor=')[1].split('&')[0]
        print('cursor:' + cursor)
        hd = int(url_data.split('hd=')[1].split('&')[0])
        print('hd:' + str(hd))
        url = get_video(cursor, url_data, hd)
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', url)
        self.send_header('Refresh', '0;url={}'.format(url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3200')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(url).encode('utf-8'))
        return None
