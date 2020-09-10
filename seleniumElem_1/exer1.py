# -*- coding: UTF-8 -*-
#author:zhaojinyu
#time:2019-11-01
'''
1. 访问天气查询网站（网址如下），查询江苏省天气
http://www.weather.com.cn/html/province/jiangsu.shtml

2. 获取江苏所有城市的天气，并找出其中每天最低气温最低的城市，显示出来，比如
温度最低为12℃, 城市有连云港 盐城
'''

from selenium import webdriver
import time
from config import CHROME_DRIVER

#加载驱动
driver = webdriver.Chrome(CHROME_DRIVER)
win = driver.get('http://www.weather.com.cn/html/province/jiangsu.shtml')

time.sleep(1)
# 得到天气列表
lm = driver.find_element_by_id('forecastID').text
# print(type(lm),lm)

# //循环将列表中的城市、最低温、最高到字典中，
'''
dic={
        ["city":"南京",“最低温”:"9℃","最高温":"20℃"],
        ["city":"苏州",“最低温”:"12℃","最高温":"20℃"],
        ["city":"苏州",“最低温”:"12℃","最高温":"20℃"],
    }
'''
# //取所有最低温，得到最低温的index，然后得到城市名称
ll = lm.split('\n')
# 用‘/’分隔温度
list=[]
list_low=[]
for i in range(len(ll)):
	if i%2==1 and i>0:
		temp=ll[i].split('/')
		dict={'city':ll[i-1],'low':temp[0],'hig':temp[1]}
		list_low.append(temp[0])
		list.append(dict)
print(list)
min = min(list_low)
for i in range(len(list)):
	if list[i]['low']==min :
		print('最低温度的最低城市是：')
		print(list[i]['city'])
		print('温度是',min)

# citynames = lm.find_elements_by_tag_name('dt')
# cityList=[]
# print('城市名称：')
# for i in citynames:
# 	cityList.append(i.text)

driver.quit()
