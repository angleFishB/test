# -*- coding: UTF-8 -*-
# @Time:2020-09-02
# @Author :Zhaojinyu
'''
打开百度新歌榜， http://music.baidu.com/top/new  此链接打不开了
自己找的链接（网易云音乐） ：https://music.163.com/#/discover/toplist?id=19723756
在排名前50的歌曲中，找出其中排名上升的歌曲和演唱者

注意： 有的歌曲名里面有 "影视原声" 这样的标签， 要去掉
最终结果显示的结果如下：
我不能忘记你       :  林忆莲
等                :  严艺丹
飞天              :  云朵
粉墨              :  霍尊
春风十里不如你     :  李健
'''
from selenium import webdriver
from config import CHROME_DRIVER,PRO_PATH
import time

def getText():
	driver = webdriver.Chrome(CHROME_DRIVER)
	#打开网易云音乐网页
	driver.get('https://music.163.com/')
	driver.implicitly_wait(5)
	#点击“排行榜”
	driver.find_element_by_id('g_nav2').find_element_by_link_text('排行榜').click()

	#切换到排行榜界面
	for handle in driver.window_handles:
		driver.switch_to.window(handle)
		time.sleep(3)
		# driver.implicitly_wait(30)  #没有加载出来就执行了*********
		if '云音乐飙升榜' in driver.title:
			break
	#切到g_iframe 中
	driver.switch_to.frame('g_iframe')
	#找到 歌曲排行榜
	topListP = driver.find_element_by_id('song-list-pre-cache')
	trs = topListP.find_elements_by_tag_name('tr')

	for tr in trs[1:]:
		#找到 上升、下降的元素
		ele = tr.find_element_by_css_selector('td>div>div .u-icn')
		if ele.get_attribute('class')=='ico u-icn u-icn-73 s-fc9':
			rank = tr.find_element_by_css_selector('td>div .num').text #排行
			songName = tr.find_element_by_css_selector('td .ttc b').get_attribute('title') #歌曲名
			singer =tr.find_element_by_css_selector('td .text ').get_attribute('title') #歌手名
			# print(f"<<20{rank}  {songName}  {singer}")
			print('{0:<3}  {1:^30} {2:>50}'.format(rank, songName, singer))
	time.sleep(5)

	driver.quit()

def pp():
	rank = '1'
	songName = '不是不可能发生'
	singer ='王菲'
	i=0
	while(i<10):
		rank =rank+'m'
		songName=songName+'p'
		singer=singer+'y'
		print('{0:<3}  {1:^30} {2:>50}'.format(rank, songName, singer))
		i=i+1

if __name__ == '__main__':
    getText()
	# pp()

