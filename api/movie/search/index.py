import requests
from http.server import BaseHTTPRequestHandler
import json


def getmovie(name):
    print(name)
    movie_page = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid={0}&mid=1&page=1&limit=1".format(name))
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    play_list = list(data['data']['list'][0]['data']['vod_play_list'].values())
    return play_list


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def index_html(url_list):
    name_list = []
    urls = []
    for i in url_list:
        name = i['player_info']['show']
        name_list.append(name)
        url = i['urls']
        urls.append(url)
    return name_list, urls


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        name = path.split('?')[1]
        data = str(index_html(getmovie(name)))
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
