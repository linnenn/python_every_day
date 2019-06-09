#! usr/bin/env python3
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from datetime import datetime,timedelta
from pymongo import MongoClient
import time
 
mongo = MongoClient()["dataanalysis"]["lagou"]
values = mongo.find({},{"_id":0,"positionAdvantage":1,"salary":1,"city":1,"positionName":1,"workYear":1,"education":1,"industryField":1,"companySize":1,"financeStage":1,"firstType":1,"secondType":1,"thirdType":1})
values = [row for row in values]
df = pd.DataFrame(values)
 
# 格式化公司规模
def length(data,type):
    value = data.values
    if not value:
        return 0
    value = value[0]
    if not value:
        return 0
    if value.find("以上") != -1:
        if type == 1:
            return 2000
        else:
            return 10000
    elif value.find("-") != -1:
        t = value.replace("人","").split("-")
        if type == 1:
            return int(t[0])
        else:
            return int(t[1])
    else:
        if type == 1:
            return 0
        else:
            return 15
        
def min_staff(data):
    return length(data,1)
 
def max_staff(data):
    return length(data,2)
 
df["min_staff"] = df[["companySize"]].apply(min_staff,axis=1)
df["max_staff"] = df[["companySize"]].apply(max_staff,axis=1)
df = df.drop(["companySize"],axis=1)
 
 
# 格式化薪资
def salary(data,type):
    value = data.values
    if not value:
        return 0
    value = value[0]
    if not value:
        return 0
    if value.find("-") != -1:
        t = value.replace("k","").replace("K","").split("-")
        if type == 1:
            return int(t[0])*1000
        elif type == 2:
            return int(t[1])*1000
        else:
            return (int(t[0])*1000+int(t[1])*1000)/2
    else:
        return 0
        
def min_salary(data):
    return salary(data,1)
 
def max_salary(data):
    return salary(data,2)
 
def avg_salary(data):
    return salary(data,3)
 
df["min_salary"] = df[["salary"]].apply(min_salary,axis=1)
df["max_salary"] = df[["salary"]].apply(max_salary,axis=1)
df["avg_salary"] = df[["salary"]].apply(avg_salary,axis=1)
 
# 格式化语言
def language(data):
    value = data.values
    if not value:
        return None
    value = value[0]
    if not value:
        return None
    value = value.upper()
    if value.find("PYTHON") != -1:
        return "python"
    if value.find("C++") != -1:
        return "c/c++"
    if value.find("C") != -1:
        return "c/c++"
    if value.find("JAVA") != -1:
        return "java"
    if value.find("PHP") != -1:
        return "php"
    return None
 
df["language"] = df[["positionName"]].apply(language,axis=1)
df = df.dropna()
