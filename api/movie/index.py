# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json


def getmovie(url):
    moviepage = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid=323854&mid=1&page=1&limit=10")
    data = moviepage.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    url = data['data']['list'][0]['data']['vod_play_list']['4']['player_info']['parse2']
    print(url)
    return url


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url = path.split('?')[1]
        data = getmovie(url)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return