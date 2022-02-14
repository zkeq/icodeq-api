# -*- coding: UTF-8 -*-
import json
import requests
from http.server import BaseHTTPRequestHandler


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def url_2_html(url):
    html_file = read_file('./api/tuostudy/temp.html')
    html_file = html_file.replace('{{url}}', url)
    return html_file


def get_308(name):
    url = 'http://tuo-site.oss-cn-beijing.aliyuncs.com/data.json'
    r = requests.get(url)
    _data = json.loads(r.text)
    try:
        url = _data[name]
    except KeyError:
        url = 'https://tuostudy.vercel.app/'
    data = url_2_html(url)
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
