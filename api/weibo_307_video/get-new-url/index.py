# coding:utf-8
import requests
import redis
from http.server import BaseHTTPRequestHandler


def get_new_url():
    r = redis.Redis(
      host='apn1-destined-giraffe-32369.upstash.io',
      port=32369,
      password='9a4bbcdc0b88484ab13ec54098ea5fb0', ssl=True)

    cookie = r.get('cookie')
    url = 'https://weibo.com/ajax/profile/getWaterFallContent?uid=3908615569&cursor=0'
    headers = {
      'Cookie': cookie,
      'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
      'X-Requested-With': 'XMLHttpRequest'}
    content = requests.get(url, headers=headers).json()
    w100w = content['data']['list'][2]['page_info']['media_info']['playback_list'][2]['play_info']['url']
    return w100w


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        data = get_new_url()
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.end_headers()
        self.wfile.write(data)
        return None
