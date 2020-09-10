# -*- coding: UTF-8 -*-
# @Time:2020-08-24
# @Author :Zhaojinyu
'''
1.search1():
	1-1.通过id找元素 driver.find_element_by_id("kw")
	1-2.输入框输入值  ele.send_keys("7xi\n")
2.search2（）：
	2-1.通过name定位元素 ele = driver.find_element_by_name('button')
	2-2.获取元素的文本  ele.text
	2-3.获取元素的html文本  href_html = driver.find_element_by_link_text('访问百度').get_attribute('href')
	2-4.通过tag获取元素组 eles = driver.find_elements_by_tag_name('option')
3.getWindows()
	3-1.获取当前窗口title  driver.title
	3-2.获取当前窗口地址栏url  driver.current_url
	3-3.截整个屏  driver.get_screenshot_as_file(PRO_PATH+'/data/'p1.png')
	3-4.截图一个元素  ele.screenshot(PRO_PATH+'/data/part.png')
'''

from selenium import webdriver
import time
from config import CHROME_DRIVER,PRO_PATH

def search1():
	#1.打开浏览器
	driver = webdriver.Chrome(CHROME_DRIVER)
	#2.打开网址
	win = driver.get('https://www.baidu.com/')
	#3.休眠3秒
	time.sleep(3)

	'''
	方法一：通过id找到元素
	'''
	# find_element_by_id 返回值是 element
	# find_elements_by_id 返回值是list
	#4.通过id找到元素
	ele = driver.find_element_by_id("kw")
	#5.往元素中输入
	ele.send_keys("7xi\n")
	print(type(ele),ele)
	time.sleep(5)
	#关闭浏览器
	driver.quit()

def search2():
	driver = webdriver.Chrome(CHROME_DRIVER)
	win = driver.get(r'D:\code_workspace\seleniumLesson\pageHTML\test.html')
	time.sleep(3)
	ele = driver.find_element_by_name('button')
	# eles = driver.find_elements_by_name('button')
	print(type(ele),ele.text)
	href_html = driver.find_element_by_link_text('访问百度').get_attribute('href')
	print(href_html)
	# ele.click('s_btn_wr')
	eles = driver.find_elements_by_tag_name('option')
	for i in eles:
		print(i.text)
	driver.quit()

def getWindows():
	driver = webdriver.Chrome(CHROME_DRIVER)
	win = driver.get(r'https://music.163.com/')
	time.sleep(1)
	#获取当前窗口title
	print('title:',driver.title)

	#获取当前窗口地址栏url
	print('url:',driver.current_url)

	#截屏
	nowtime = time.strftime("%Y%m%d%H%M%S", time.localtime()) #获取当前时间，返回类型为str，格式20200828155529
	# driver.get_screenshot_as_file(PRO_PATH+'/data/'+nowtime+'.png')#截取整个页面
	ele = driver.find_elements_by_class_name('ban-img')
	print(ele)
	#截取单个元素---fail
	# ele.screenshot(PRO_PATH+'/data/part-'+nowtime+'.png')
	driver.quit()
def for_back():
	driver = webdriver.Chrome(CHROME_DRIVER)
	win = driver.get(PRO_PATH+'/pageHTML/test.html')
	time.sleep(1)
	ele = driver.find_element_by_name('button2')
	ele.click()
	print('1.click')
	time.sleep(2)
	driver.back()
	print('2.后退')
	time.sleep(2)
	driver.forward()
	print('3.前进')
	time.sleep(2)

	driver.quit()

if __name__ == '__main__':
	# search1()
	# search2()
	# getWindows()
	for_back()