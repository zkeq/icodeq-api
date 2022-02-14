# -*- coding: UTF-8 -*-
import requests
from http.server import BaseHTTPRequestHandler


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def url_2_html(url):
    html_file = read_file('./api/tuostudy/temp.html')
    url = url.replace('\n', '')
    html_file = html_file.replace('{{url}}', url)
    return html_file


def get_308(name):
    url = 'http://tuo-site.oss-cn-beijing.aliyuncs.com/index.txt'
    r = requests.get(url)
    r.encoding = 'utf-8'
    _str = r.text
    _list = _str.split('\n')
    name_list = []
    url_list = []
    for i in _list:
        line_list = i.split('|||')
        name_list.append(line_list[0])
        url_list.append(line_list[1])
    final_url = 'https://tuostudy.vercel.app/'
    for i in name_list:
        if i == name:
            final_url = url_list[name_list.index(i)]
    data = url_2_html(final_url)
    return data


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        user = path.split('?')[1]
        data = get_308(user)
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(data.encode('utf-8'))
        return
