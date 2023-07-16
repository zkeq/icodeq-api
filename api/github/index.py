# -*- coding: UTF-8 -*-
import requests
import re
from http.server import BaseHTTPRequestHandler
import json


def list_split(items, n):
    return [items[i:i + n] for i in range(0, len(items), n)]


def get_data(name):
    gitpage = requests.get("https://github.com/" + name)
    data = gitpage.text
    data_date_reg = re.compile(r'data-date="(.*?)" data-level')
    data_count_reg = re.compile(r'<span class="sr-only">(.*?) contribution')
    data_date = data_date_reg.findall(data)
    data_count = data_count_reg.findall(data)
    data_count = list(map(int, [0 if i == "No" else i for i in data_count]))
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


def error_403(path, user,msg):
    data = """<?xml version="1.0" encoding="UTF-8"?>
    <Error>
      <Code>AccessDenied</Code>
      <Message>Please enter the correct parameters.</Message>
      <RequestId>{0}</RequestId>
      <HostId>{1}</HostId>
      <ApiName>{2}</ApiName>
    </Error>
    """.format(path, 'GitHub-Calendar', user).encode("utf-8")
    code = 403
    data_type = 'application/xml'
    print(msg, user)
    return code, data, data_type


print(get_data("zkeq"))
