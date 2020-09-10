# -*- coding: UTF-8 -*-
# @Time:2020-08-28
# @Author :Zhaojinyu
from selenium import webdriver
from config import CHROME_DRIVER,PRO_PATH
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def switch_window():
    driver = webdriver.Chrome(CHROME_DRIVER)
    win = driver.get('https://www.baidu.com/')
    ele = driver.find_element_by_id('kw')
    ele.send_keys('网易云音乐\n')
    driver.implicitly_wait(60)
    # driver.get_screenshot_as_file(PRO_PATH+'\data\music.png')
    driver.find_element_by_link_text('网易云音乐').click()
    for handle in  driver.window_handles:
        win = driver.switch_to.window(handle)
        if   driver.title=='网易云音乐' :
            print(type(handle),'enter music')
            print(handle)
            time.sleep(10)
            driver.get_screenshot_as_file(PRO_PATH + '\data\pp1.png')

            break

    # print(driver.window_handles)
    # print(type(driver.window_handles))

    driver.quit()

def wait():
    driver = webdriver.Chrome(CHROME_DRIVER)
    win = driver.get('https://music.163.com/')
    driver.implicitly_wait(10)
    driver.switch_to.frame ('contentFrame')
    ele = driver.find_element_by_id('index-banner')
    ele.screenshot(PRO_PATH+r'\data\banner.png')
    print(ele.text)

    driver.switch_to.default_content()

    #显式等待
    ele = WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CLASS_NAME ,'username')))

    #当元素可以被点击时，进入下一步，最大等待时间是30秒
    elel2 = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.CLASS_NAME ,'username')))

def switch_frame():
    driver = webdriver.Chrome(CHROME_DRIVER)
    driver.get('https://music.163.com/')
    driver.implicitly_wait(5)
    driver.find_element_by_id('g_nav2').find_element_by_link_text('排行榜').click()
    # print(driver.window_handles)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        time.sleep(3)
        # driver.implicitly_wait(30)  #没有加载出来就执行了*********
        print('=======',driver.title)
        if '云音乐飙升榜' in driver.title:
            break
    driver.get_screenshot_as_file(PRO_PATH+'/data/biaos.png')
    driver.switch_to.frame(1)
    # driver.get_screenshot_as_file(PRO_PATH + '/data/fr2.png')
    # eiel=driver.find_element_by_tag_name('frame').screenshot(PRO_PATH+'/data/fr1.png')

    # driver.find_elements_by_id('song-list-pre-cache')
    time.sleep(10)
    driver.quit()

def switch_frame2():
	driver = webdriver.Chrome(CHROME_DRIVER)
	driver.get(PRO_PATH+'/pageHTML/frame.html')
	# driver.switch_to.frame('frame1')
	# driver.find_element_by_tag_name('input').send_keys('nei 1 c')
	# driver.switch_to.frame('frame2')
	# driver.find_element_by_tag_name('input').send_keys('nei 2 c')
	driver.switch_to.frame(1)
	driver.find_element_by_tag_name('input').send_keys('第2个')

	#切回主html
	# driver.switch_to.default_content()

	driver.switch_to.parent_frame()
	driver.find_element_by_tag_name('input').send_keys('最外面')
	driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
	driver.find_element_by_tag_name('input').send_keys('内一层')
	driver.switch_to.frame('frame2')
	driver.find_element_by_tag_name('input').send_keys('内二层')
	time.sleep(4)
	driver.switch_to.parent_frame()
	driver.find_element_by_tag_name('input').send_keys('内一层222')


	time.sleep(8)
	driver.quit()

if __name__ == '__main__':
    switch_frame2()