#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import re,time,requests
from requests.exceptions import ReadTimeout,HTTPError,RequestException,ConnectionError
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
def estimate_time(ip_test_date,ip_rest_time):#rest_time+test_date-current_time
    new_ip_test_date='20'+ip_test_date+':00'
    time_stamp = time.mktime(time.strptime(new_ip_test_date, '%Y-%m-%d %H:%M:%S'))
    d_ip_rest_time=re.findall('\d',ip_rest_time)
    a_ip_rest_time=re.findall('\D',ip_rest_time)
    if a_ip_rest_time[0]=='分钟':
        da_ip_rest_time=int(d_ip_rest_time[0])*60
    elif a_ip_rest_time[0]=='小时':
        da_ip_rest_time = int(d_ip_rest_time[0]) * 3600
    else:
        da_ip_rest_time = int(d_ip_rest_time[0]) * 86400
    result_time=time_stamp+da_ip_rest_time-time.time()
    return result_time
def status_code(ip_type,ip_add,ip_port):
    proxies = {
        "%s" % ip_type: "%s://%s:%s" % (ip_type, ip_add, ip_port)
    }
    try:
        response = requests.get("https://www.baidu.com", proxies=proxies, timeout=2)
        return response.status_code
    except ReadTimeout:
        return ('Timeout')
    except HTTPError:
        return ('Timeout')
    except RequestException:
        return ('Timeout')
    except ConnectionError:
        return ('Timeout')
try:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    browser = webdriver.Chrome(options=chrome_options)
    browser.get("http://www.xicidaili.com/nn")
    html=browser.page_source
    browser.quit()
except TimeoutException:
    print('Time Out')
dict_http={}
dict_https={}
soup=BeautifulSoup(html,'lxml')
lists=soup.tbody.contents
count=0
while count<199:
    count+=2
    need_jiexi=str(lists[count])
    pattern=re.compile('<td>(.*?)</td>',re.S)
    items=re.findall(pattern,need_jiexi)
    pattern2=re.compile('<div class="bar_inner fast" style="width:(.*?)%">',re.S)
    items2=re.findall(pattern2,need_jiexi)
    ip_place_list=re.findall('<a href.*?">(.*?)</a>',items[2])
    if len(ip_place_list)==1:
        ip_place = ip_place_list[0]
    else:
        continue
    if len(items2)==2:
        ip_speed = items2[0]
        ip_connect_time = items2[1]
        if int(ip_speed) and int(ip_connect_time) > 79:
            ip_speed=ip_speed
            ip_connect_time=ip_connect_time
        else:
            continue
    else:
        continue
    ip_rest_time = items[4]
    ip_test_date = items[5]
    if estimate_time(ip_test_date,ip_rest_time)>1020:
        ip_test_date=ip_test_date
        ip_rest_time=ip_rest_time
    else:
        continue
    ip_type = items[3].lower()
    ip_add = items[0]
    ip_port = items[1]
    if status_code(ip_type,ip_add,ip_port)==200:
         ip_type = ip_type
         ip_add = ip_add
         ip_port = ip_port
    else:
         continue
    if ip_type == 'http':
        name = 'ip_address_%d' % (len(dict_http) + 1)
        dict_http.update({name: [ip_add, ip_port, ip_place]})
    else:
        name = 'ip_address_%d' % (len(dict_https) + 1)
        dict_https.update({name: [ip_add, ip_port, ip_place]})
print('http:',dict_http)
print('https:',dict_https)