#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3

import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime,timedelta
from pymongo import MongoClient
import time, requests, json, jsonpath
import urllib 
import os

def downloader(city, keyword, page):
    '''
    :param city:
    :param keyword:
    :param page:
    :return:
    '''
    url = "https://www.lagou.com/jobs/positionAjax.json?city={}&needAddtionalResult=false".format(urllib.parse.quote(city))
    data = {
        "first": "true",
        "pn": page,
        "kd": keyword
    }
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Content-Length": "26",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Host": "www.lagou.com",
        "Cookie": "WEBTJ-ID=20190114141014-1684afb5fb641a-0264531f631492-10306653-1296000-1684afb5fb72fa; _ga=GA1.2.1603350619.1547446216; _gid=GA1.2.1722882028.1547446216; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547446216; user_trace_token=20190114141019-11ffe994-17c3-11e9-af0a-525400f775ce; LGUID=20190114141019-11ffed80-17c3-11e9-af0a-525400f775ce; JSESSIONID=ABAAABAAAIAACBIF3714583E10DD68BED6CDB0C421599DA; TG-TRACK-CODE=index_navigation; LGRID=20190114142153-af672943-17c4-11e9-af0b-525400f775ce; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1547446913; index_location_city=%E5%8C%97%E4%BA%AC; SEARCH_ID=1a6b191342914e43924e821e203a57d8",
        "Origin": "https://www.lagou.com",
        "Referer": "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "X-Anit-Forge-Code": "0",
        "X-Anit-Forge-Token": "None",
        "X-Requested-With": "XMLHttpRequest"
    }
    proxies = {
        "http": "****",
        "https": "****",
    }
    # while True:
    try:
        print(url)
        response = requests.post(url, data=data, headers=headers)
        response.encoding = "utf-8"
        print('statusCode: {}'.format(response.status_code))
        print(response.text)
        if response.status_code == 200:
            data = json.loads(response.text)
            result = jsonpath.jsonpath(data, "$.content.positionResult.result")[0]
            Client = MongoClient()
            with Client.dataanalysis as mongo:
                lagou = mongo.lagou
                for row in result:
                    row["_id"] = "{}".format(row["positionId"])
                    lagou.update_one({"_id": row["_id"]}, {"$set": row}, upsert=True)
                    print("update or insert data = {}".format(row["_id"]))
    except BaseException as e:
        print(e)
if __name__ == "__main__":
    print('begin!')
    keyword = 'php'
    secs = 3
    page = 1
    for city in ['北京','上海','广州','深圳']:
        # for page in range(0,20):
        print((city,keyword,page))
        downloader(city,keyword,page)
        print('inner sleep: {}'.format(secs))
        time.sleep(secs)
    print('outer sleep: {}'.format(secs))
    time.sleep(secs)