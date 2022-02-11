# -*- coding: UTF-8 -*-
import requests
from http.server import BaseHTTPRequestHandler
from urllib.parse import unquote
import json
import time


# 获取时间戳
def get_timestamp():
    return time.time()


def getmovie():
    movie_page = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid=323854&mid=1&page=1&limit=1")
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    url_str = data['data']['list'][0]['data']['vod_play_list']['4']['player_info']['parse2']
    url_str = url_str.replace('..', '.')
    url_list = url_str.split(',')
    print(url_list)
    return url_list


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def index_html(url_list, begin_time):
    html = read_file('./api/movie/main.html')
    html = html.replace('{0}', url_list[0])
    html = html.replace('{1}', url_list[1])
    html = html.replace('{2}', url_list[2])
    final_time = get_timestamp()
    run_time = str(final_time - begin_time)
    print(run_time)
    html = html.replace('{time}', run_time)
    return html


def movie_search(name):
    movie_page = requests.get("http://aliyun.k8aa.com:80/mogai_api.php/v1.vod?page=1&limit=10&wd=" + name)
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    total = data['data']['total']
    limit = data['data']['limit']
    min_num = min(total, limit)
    movie_name = []
    movie_code = []
    movie_content = []
    for i in range(min_num):
        movie_name.append(data['data']['list'][i]['vod_name'])
        movie_code.append(data['data']['list'][i]['vod_id'])
        movie_content.append(data['data']['list'][i]['vod_content'])
    print(movie_name)
    return {'total': total, 'movie_name': movie_name, 'movie_code': movie_code, 'movie_content': movie_content, 'min_num': min_num}


def get_search_html(name, dict_all, begin_time):
    url_root = 'https://api.icodeq.com/api/movie/search?'
    html = read_file('./api/movie/search.html')
    html = html.replace('{0}', unquote(name, 'utf-8'))
    final_time = get_timestamp()
    run_time = str(final_time - begin_time)
    print(run_time)
    html = html.replace('{time}', run_time)
    for i in range(dict_all['min_num']):
        n = i + 1
        html = html.replace('{%s}' % n, dict_all['movie_name'][i])
        html = html.replace('{%s_code}' % n, url_root + str(dict_all['movie_code'][i]))
        html = html.replace('{%s_content}' % n, dict_all['movie_content'][i])
    return html


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        begin_time = get_timestamp()
        path = self.path
        url_split = path.split('?')
        if len(url_split) == 1:
            data = index_html(getmovie(), begin_time)
        elif len(url_split) == 2:
            data = get_search_html(url_split[1], movie_search(url_split[1]), begin_time)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
