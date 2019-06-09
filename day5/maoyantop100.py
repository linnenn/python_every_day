#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from bs4  import BeautifulSoup
import pandas as pd
import requests

headers = {
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}
url = 'https://maoyan.com/board/4'
request = requests.get(url,headers=headers)

'''
	获取猫眼电影前100条数据
'''
rest = BeautifulSoup(request.text,'html.parser')
print(rest)