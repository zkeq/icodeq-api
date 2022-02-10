# -*- coding: UTF-8 -*-
import requests
import re
import pickle
from http.server import BaseHTTPRequestHandler
import json
import os


def getmovie():
    moviepage = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid=323854&mid=1&page=1&limit=10")
    data = moviepage.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    url_str = data['data']['list'][0]['data']['vod_play_list']['4']['player_info']['parse2']
    url_str = url_str.replace('..', '.')
    url_list = url_str.split(',')
    return url_list


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def index_html(url_list):
    html = read_file('./api/movie/main.html')
    html = html.replace('{0}', url_list[0])
    html = html.replace('{1}', url_list[1])
    html = html.replace('{2}', url_list[2])
    return html


def get_search_html(name):
    
    return 1


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_split = path.split('?')
        if len(url_split) == 1:
            data = index_html(getmovie())
        if len(url_split) == 2:
            data = get_search_html(url_split[1])
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
