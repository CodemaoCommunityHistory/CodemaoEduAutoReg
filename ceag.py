# @author Wangs_official
import concurrent.futures
import time
import requests
import os
import json
import openpyxl
import random

def get_class(token):
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
    url = f"https://eduzone.codemao.cn/edu/zone/classes?page=1&TIME={int(time.time())}"
    req = requests.get(url=url, headers=header)
    if req.status_code == 200:
        return str(json.loads(req.text).get("total"))
    else:
        print(f"请求失败：{req.text}")
        return False


def create_class(token):
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
    li = []
    for i in range(12):
        temp = random.randrange(65, 91)
        c = chr(temp)
        li.append(c)
    result = "".join(li)
    wc_name = f"{result}"
    req = requests.post("https://eduzone.codemao.cn/edu/zone/class", data=json.dumps({"name": wc_name}), headers=header)
    if req.status_code == 200:
        id = json.loads(req.text).get("id")
        stud_names = json.dumps({"student_names": ["vlokud", "mgstop", "waidtk", "ruabon", "ncxjsb", "apgtxw", "sqnpfx",
                                                   "qvxpgr", "yihsdm", "vzgsub", "fxywlt", "smqwvt", "qdrjoe", "rohgzt",
                                                   "fpzuvd", "zfcuhy", "kfmlsd", "uxdwsc", "qyvkle", "vstunq", "pqbcjx",
                                                   "hcxfyd", "caewzx", "obaxfu", "qfobkc", "inrdqg", "ftizlb", "jahdoz",
                                                   "himayz", "fdrjnv", "lzjxpd", "lzqguo", "zvywpa", "batmqp", "vdtgzf",
                                                   "qihpke", "lgdtxn", "mevsfn", "gkpzth", "naxtby", "oejtmv", "vpwbga",
                                                   "twfpav", "mabxio", "zbhyoc", "xgfshv", "zumfnp", "tmajfv", "qtwzma",
                                                   "fozhjb", "sgaouk", "odkxzy", "hkexpl", "byuzpc", "vjlxsh", "gdczwr",
                                                   "urhtav", "txyjrc", "oalhkz", "yfkxbg", "mliqdx", "osqxck", "adbtro",
                                                   "qdzfeb", "ldjvuw", "glhkns", "flevyk", "lrkxta", "lamjey", "fphkcr",
                                                   "hxolyc", "euvdmh", "vpdkue", "bqonci", "fmibrj", "zfvjcm", "efhyvj",
                                                   "ljguwc", "ckamsg", "hwlned", "utzxer", "mtdnwy", "xitflg", "xgdofl",
                                                   "gvirnt", "zvbkos", "gvcjhi", "wqceok", "lvhnto", "caurnj", "xhwnfl",
                                                   "qeykzn", "tkefna", "hbamgv", "sinrpq", "xponme", "zpwquc", "hebomj",
                                                   "bzsxlp", "mjcotf"]})
        req2 = requests.post(f"https://eduzone.codemao.cn/edu/zone/class/{id}/students", data=stud_names,
                            headers=header)
        if req2.status_code == 200:
            with open(f"xls/{id}.xls" , "wb") as f:
                f.write(req2.content)
            return True
        else:
            print(f"请求失败：{req2.text}")
            return False
    else:
        print(f"请求失败：{req.text}")
        return False


if __name__ == "__main__":
    itoken = input("请输入账户Token:  ")
    print("将以12个字母作为班级名称，且将学生信息保存到当前目录下的 xls 文件夹，八线程启动")
    try:
        hm = int(get_class(itoken))
    except TypeError:
        exit("请求失败")
    wc = 400 - hm
    createc = 0
    print(f"将创建{wc}个班级")
    for _ in range(int(wc)):
        with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(create_class, itoken)]
            for future in concurrent.futures.as_completed(futures):
                createc += 4
                print(f"\r请稍后，正在创建中，已创建{createc}个", end="")
                if createc == wc:
                    exit("全部创建完成")
                if future.result() is False:
                    exit()


