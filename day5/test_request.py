#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import json
from bs4 import BeautifulSoup
import re
#
#
#get post put delete options head 
#
headers = {
	"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
}

cookies = dict(cookies_are='working')
result = requests.post('https://www.ithome.com/0/425/182.htm',headers=headers)
# json_str = json.dumps(data)
# print(json.loads(json_str))
result.encoding = 'utf-8'
# print(result.apparent_encoding)
res = result.text
parse_str = BeautifulSoup(res,'html.parser')
# print(parse_str.a)
# print(parse_str.head.contents)
# for item in parse_str.head.children:
	# print(item)
	# 
# print(parse_str.head.children)
# print(parse_str.a.attrs)
# a标签里的内容实际上是注释，但是如果我们利用.string 来输出它的内容，我们发现它已经把注释符号去掉了，所以，我们在使用前最好做一下判断是不是注释:
# if type(parse_str.a.string) == bs4.element.Comment://只有是注释的时候才可以有下面的操作
# print(parse_str.a.string)

# print(parse_str.a.name)

res = parse_str.find('a',id=None)
# for a_item in res:
	# print(a_item)
for item in parse_str.select('a[target="_blank"]'):
	print(item)