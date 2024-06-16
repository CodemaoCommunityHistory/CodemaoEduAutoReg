# @author Wangs_official
import time
import requests
import os
import json
import openpyxl

def get_class(token     ):
    header = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36",
        "Authorization": f"Bearer {token}"
    }
    url = f"https://eduzone.codemao.cn/edu/zone/classes?page=1&TIME={int(time.time)}"
    req = requests.get(url=url, headers=header)
    if req.status_code == 200:
        return str(json.loads(req.text).get("total"))
    else:
        print(f"请求失败：{req.text}")
        return False

def create_class(token,name):
    pass