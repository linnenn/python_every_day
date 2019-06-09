#! usr/bin/env python3

import re

total_x = None
total_y = []
total_city = []
for city_name,data in df.groupby(by="city"):
    result = data.groupby(by=["language"])["avg_salary"].mean().sort_index()
 
    plt.figure(figsize=(20,8),dpi=80)
 
    _x = result.index
    _y = result.values
    plt.bar(_x,_y)
    
    total_x = _x
    total_y.append(_y)
    total_city.append(city_name)
 
    plt.xlabel("语言")
    plt.ylabel("平均薪资")
    plt.title("{}地区编程语言平均薪资".format(city_name))
 
    plt.grid()
    plt
#salary compare
plt.figure(figsize=(20,8),dpi=80)
 
interval = 6
ind = np.array(range(0,len(total_x) * interval,interval))
width = 1
for index in range(len(total_city)):
    plt.bar(ind - (2 - index) * width + width/2,total_y[index],label=total_city[index],width=1)
 
plt.xticks(range(0,len(total_x) * interval,interval),total_x)
plt.xlabel("语言")
plt.ylabel("平均薪资")
plt.title("一线城市编程语言平均薪资")
 
plt.grid()
plt.legend()
plt

#compare

def position_advantage(data):
    value = data.values
    if not value:
        return []
    value = value[0]
    if not value:
        return []
    value = re.sub(r"[.~]","",value)
    return re.split(r'[,，； ;、+-]',value)
labels = list(set([i for row in df[["positionAdvantage"]].apply(position_advantage,axis=1).values for i in row if i]))
position_data = pd.DataFrame(np.zeros((df.shape[0],len(labels))).astype(int),columns=labels,index=df.index)
for label in labels:
    position_data[label][df["positionAdvantage"].str.contains(label)] = 1
 
result = position_data.sum().sort_values(ascending=False)
 
size = result[:10].values
size = [row for row in size]
labels = result[:10].index
labels = [row for row in labels]
size.append(result.sum() - sum(size))
labels.append("其它")
explode = [0 for i in range(len(size))]
explode[0] = 0.1
 
plt.figure(figsize=(10,10),dpi=80)
plt.pie(size, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
plt.title("岗位优势百分比")
plt
#city compate

total_value = []
total_label = []
labels = [row for row in result[:10].index]
for index in range(len(total_city)):
    city = total_city[index]
    data = position_data[df["city"] == city]
    total_size = data.sum().sum()
    
    total_label.append(city)
    total_value.append((data[labels].sum()/total_size*10000).values.tolist())
 
plt.figure(figsize=(20,8),dpi=80)
 
interval = 8
ind = np.array(range(0,len(labels) * interval,interval))
width = 1
for index in range(len(total_label)):
    plt.bar(ind - (2 - index) * width + width/2,total_value[index],label=total_label[index],width=1)
 
plt.xticks(range(0,len(labels) * interval,interval),labels)
plt.xlabel("福利")
plt.ylabel("占比(*100)")
plt.title("岗位优势占比图")
 
plt.grid()
plt.legend()
plt

#工作经验要求占比
for city_name,data in df.groupby(by="city"):
    result = data.groupby(by=["workYear"])["avg_salary"].count().sort_values()
 
    plt.figure(figsize=(8,8),dpi=80)
 
    _x = result.index
    _y = result.values
    plt.pie(_y, labels=_x, autopct='%1.1f%%',shadow=True, startangle=90)
 
    plt.title("{}地区编程语言学历要求占比".format(city_name))
 
    plt.grid()
    plt

#学历要求占比
for city_name,data in df.groupby(by="city"):
    result = data.groupby(by=["education"])["avg_salary"].count().sort_index()
 
    plt.figure(figsize=(8,8),dpi=80)
 
    _x = result.index
    _y = result.values
    plt.pie(_y, labels=_x, autopct='%1.1f%%',shadow=True, startangle=90)
 
    plt.title("{}地区编程语言学历要求占比".format(city_name))
 
    plt.grid()
    plt