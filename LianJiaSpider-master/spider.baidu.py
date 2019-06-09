#! /usr/bin/env python3

import urllib.request
import urllib
import ssl
# 用ssl创建未经验证的上下文，在url,全局不做https验证
ssl._create_default_https_context = ssl._create_unverified_context

# web = 'https://www.baidu.com'

# data = urllib.request.urlopen(web)
# print(type(data))
# print(data.getcode())
# data = data.read().decode('utf-8')
# with open('baidu.html', 'wb') as f:
# 	f.write(str.encode(data))
# 生成首页
data = {}
data['word'] = '课程'
url = 'http://www.cnblogs.com/wupeiqi/articles/4731930.html'

data = urllib.parse.urlencode(data)

fullurl = url + data

data = urllib.request.urlopen(fullurl).read()

data = data.decode('utf-8')

with open('课程.html','wb') as f:
	f.write(str.encode(data))