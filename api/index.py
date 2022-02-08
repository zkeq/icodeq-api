# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def get_data(name):
    gitpage = requests.get("https://github.com/" + name)
    data = gitpage.text
    data_date_reg = re.compile(r'data-date="(.*?)" data-level')
    data_count_reg = re.compile(r'data-count="(.*?)" data-date')
    data_date = data_date_reg.findall(data)
    data_count = data_count_reg.findall(data)
    data_count = list(map(int, data_count))
    contributions = sum(data_count)
    data_list = []
    for index, item in enumerate(data_date):
        item_list = {"date": item, "count": data_count[index]}
        data_list.append(item_list)
    data_list_split = list_split(data_list, 7)
    return_data = {
        "total": contributions,
        "contributions": data_list_split
    }
    return return_data


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        path = self.path
        try:
            user = path.split('?')[1]
        except IndexError as e:
            user = None
        if user:
            data = get_data(user)
            code = 200
            print("成功获取到Github日历：", user)
            data = json.dumps(data).encode('utf-8')
        else:
            data = """<?xml version="1.0" encoding="UTF-8"?>
<Error>
  <Code>AccessDenied</Code>
  <Message>Please enter the correct parameters.</Message>
  <RequestId>{0}</RequestId>
  <HostId>{1}</HostId>
  <ApiName>{2}</ApiName>
</Error>""".format(path, 'GitHub-Calendar', user)
            code = 403
            print("获取Github日历失败：", user)
        self.send_response(code)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(data)
        return
