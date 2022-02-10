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


def movie_search(name):
    movie_page = requests.get("http://aliyun.k8aa.com:80/mogai_api.php/v1.vod?page=1&limit=10&wd=" + name)
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    total = data['data']['total']
    movie_name = []
    movie_code = []
    movie_content = []
    for i in range(total):
        movie_name.append(data['data']['list'][i]['vod_name'])
        movie_code.append(data['data']['list'][i]['vod_id'])
        movie_content.append(data['data']['list'][i]['vod_content'])
    return {'total': total, 'movie_name': movie_name, 'movie_code': movie_code, 'movie_content': movie_content}


def get_search_html(name, dict_all):
    url_root = 'https://api.icodeq.com/api/movie/search?'
    html = read_file('./api/movie/search.html')
    html = html.replace('{0}', name)
    for i in range(dict_all['total']):
        html = html.replace('{%s}' % i, dict_all['movie_name'][i])
        html = html.replace('{%s_code} % i ', url_root + dict_all['movie_code'][i])
        html = html.replace('{%s_content} % i ', dict_all['movie_content'][i])
    return html


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_split = path.split('?')
        if len(url_split) == 1:
            data = index_html(getmovie())
        if len(url_split) == 2:
            data = get_search_html(url_split[1], movie_search(url_split[1]))
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
