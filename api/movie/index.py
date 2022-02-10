# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json

# html_template =

def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def getmovie(url):
    movie_page = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid=323854&mid=1&page=1&limit=10")
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    url_str = data['data']['list'][0]['data']['vod_play_list']['4']['player_info']['parse2']
    url_list = url_str.split(',')
    print(url_list)
    return url_list


def get_search(keyword):

    html_data = 123
    return html_data


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url = path.split('?')[1]
        search_name = path.split('?')[2]
        if search_name:
            data = get_search(search_name)
        else:
            data = getmovie(url)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode('utf-8'))
        return