import requests
from http.server import BaseHTTPRequestHandler
import json


def getmovie(name):
    movie_page = requests.get("http://aliyun.k8aa.com/mogai_api.php/v1.comment?rid={0}&mid=1&page=1&limit=1".format(name))
    data = movie_page.text
    # 解析json
    data = json.loads(data)
    # 获取视频地址
    try:
        play_list = list(data['data']['list'][0]['data']['vod_play_list'].values())
    except:
        movie_page = requests.get("http://aliyun.k8aa.com:80/mogai_api.php/v1.vod/detail?vod_id={0}&rel_limit=1".format(name))
        data = movie_page.text
        # 解析json
        data = json.loads(data)
        play_list = list(data['data']['vod_play_list'])
    return play_list


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        _html = f.read()
    return _html


def index_html(url_list):
    name_list = []
    url_final = []
    address_list = []
    urls = []
    for i in url_list:
        name = i['player_info']['show']
        address = i['player_info']['parse2']
        if address:
            address = address.replace('..', '.')
            address_list_temp = address.split(',')
            address_list_temp.insert(0, '请将下面的地址拼接起来使用')
            address_list_temp = '\n'.join(address_list_temp)
            address_list.append(address_list_temp)
        else:
            address = '下面的列表就是播放地址'
        name_list.append(name)
        url = i['urls']
        url_temp = []
        for i in url:
            try:
                name = url.get(i).get('name')
                _url = url.get(i).get('url')
            except:
                name = i.get('name')
                _url = i.get('url')
            url_temp.append(name+'<br>'+_url)
        url_temp = '\n'.join(url_temp)
        url_final.append(url_temp)
    html = read_file('./api/movie/list.html')
    for i in range(len(url_final)):
        n = i+1
        html = html.replace('{%s}' % n, name_list[i])
        html = html.replace('{%s_url}' % n, url_final[i])
        html = html.replace('{%s_address}' % n, address_list[i])
    # print(urls)
    return html


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
