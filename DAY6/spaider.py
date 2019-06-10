#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
脚本功能说明：
    获取西祠代理公布的代理ip，http://www.xicidaili.com
    保存ip到csv文件（，可以保存到数据库，第一版先不实现）
    为了防止ip被封锁，每次请求之后都会使用上次循环的第一个代理ip作为请求代理ip
    此脚本可以随意分发，但是必须加上出处！
    O(∩_∩)O谢谢！
    个人博客：http://www.zhulanchun.com
    github:https://github.com/linnenn
    gitee:https://gitee.com/JupiterAndMars_admin
    qq:944677073
'''
from bs4 import BeautifulSoup
import re,time,requests,csv
from requests.exceptions import ReadTimeout,HTTPError,RequestException,ConnectionError
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# 评估时间
class EstimateIp:
    def __init__(self, start_page=1, end_page=200):
        self.start_page = start_page
        self.end_page = end_page

    def estimate_time(self, ip_test_date, ip_rest_time):
        #rest_time+test_date-current_time
        new_ip_test_date = '20'+ip_test_date+':00'
        time_stamp = time.mktime(time.strptime(new_ip_test_date, '%Y-%m-%d %H:%M:%S'))
        d_ip_rest_time = re.findall('\d', ip_rest_time)
        a_ip_rest_time = re.findall('\D', ip_rest_time)
        if a_ip_rest_time[0]=='分钟':
            da_ip_rest_time=int(d_ip_rest_time[0])*60
        elif a_ip_rest_time[0]=='小时':
            da_ip_rest_time = int(d_ip_rest_time[0]) * 3600
        else:
            da_ip_rest_time = int(d_ip_rest_time[0]) * 86400
        result_time=time_stamp+da_ip_rest_time-time.time()
        return result_time

    # 检测ip状态，评估是否好用
    def status_code(self,ip_type,ip_add,ip_port):
        proxies = {
            "%s" % ip_type: "%s://%s:%s" % (ip_type, ip_add, ip_port)
        }
        try:
            response = requests.get("https://www.baidu.com", proxies=proxies, timeout=2)
            return response.status_code
        except ReadTimeout:
            return ('Timeout',)
        except HTTPError:
            return ('Timeout',)
        except RequestException:
            return ('Timeout',)
        except ConnectionError:
            return ('Timeout',)

    # 保存数据到csv
    def slave_to_csv(self,datas):
        headers = ['ip地址', '端口', '地址']
        rows = []
        for key,value in datas.items():
            rows.append(value)
        with open('ip_csv.csv','w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerows(rows)
    # 爬虫开启
    def web_spaider(self):
        # 先获取前20页
        handler_html = []
        for num in range(self.start_page, self.end_page):
            try:
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--headless')
                chrome_options.add_argument('--disable-gpu')
                browser = webdriver.Chrome(options=chrome_options)
                browser.get("http://www.xicidaili.com/nn")
                html = browser.page_source
                handler_html.append(html)
                browser.quit()
            except TimeoutException:
                return 'Time Out'
        return handler_html

    def analsis_html(self):
        for html in self.web_spaider():
            dict_http = {}
            dict_https = {}
            soup = BeautifulSoup(html, 'lxml')
            lists = soup.tbody.contents
            count = 0
            while count < 199:
                count += 2
                need_jiexi = str(lists[count])
                pattern = re.compile('<td>(.*?)</td>', re.S)
                items = re.findall(pattern, need_jiexi)
                pattern2 = re.compile('<div class="bar_inner fast" style="width:(.*?)%">', re.S)
                items2 = re.findall(pattern2, need_jiexi)
                ip_place_list = re.findall('<a href.*?">(.*?)</a>', items[2])
                if len(ip_place_list) == 1:
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
                if estimate_time(ip_test_date, ip_rest_time) > 1020:
                    ip_test_date = ip_test_date
                    ip_rest_time = ip_rest_time
                else:
                    continue
                ip_type = items[3].lower()
                ip_add = items[0]
                ip_port = items[1]
                if status_code(ip_type, ip_add, ip_port) == 200:
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


if __name__ == '__main__':

    print('http:',dict_http)
    slave_to_csv(dict_http)
    print('https:',dict_https)