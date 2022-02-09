# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def getmovie(url):
    moviepage = requests.get("http://47.100.138.210:91/home/api?type=ys&uid=7103652&key=afhiknorswzEFIL569&url=" + url)
    data = moviepage.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    url = data['url']
    print(url)
    return url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url = path.split('?url=')[1]
        data = getmovie(url)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return