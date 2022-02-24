# coding:utf-8

import redis
from http.server import BaseHTTPRequestHandler
import os

env_dist = os.environ
PASSWORD = env_dist.get('PASSWORD')

r = redis.Redis(
    host='apn1-destined-giraffe-32369.upstash.io',
    port=32369,
    password=PASSWORD, ssl=True)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        video_id = path.split('?')[1]
        video_url = r.get('163_mv_' + video_id).decode('utf-8')
        self.send_response(308)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('location', video_url)
        self.send_header('Refresh', '0;url={}'.format(video_url))
        self.send_header('Cache-Control', 'max-age=0, s-maxage=60, stale-while-revalidate=3600')
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('Redirecting to {} (308)'.format(video_url).encode('utf-8'))
        return None