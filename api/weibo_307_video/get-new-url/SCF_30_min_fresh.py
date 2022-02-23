# -*- coding: utf8 -*-
# 请您设置30分钟刷新一次
import requests


def get_video():
    url = 'https://api.icodeq.com/api/weibo_307_video/get-new-url'
    video_url = requests.get(url).text
    return video_url


def main_handler(event, context):
    content = get_video()
    return content
