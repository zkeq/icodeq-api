import requests
from http.server import BaseHTTPRequestHandler
import json


def getmovie(name):
    moviepage = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid=%s&mid=1&page=1&limit=1" % name)
    data = moviepage.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    play_list = list(data['data']['list'][0]['data']['vod_play_list'].values())
    print(play_list)
    return play_list


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def index_html(url_list):
    # html = read_file('./api/movie/main.html')
    play_list = url_list
    return play_list


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        url_split = path.split('?')
        data = index_html(getmovie())
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
