# -*- coding: UTF-8 -*-
# @Time:2020-08-25
# @Author :Zhaojinyu
import os,inspect
#chrome driver 的路径
CHROME_DRIVER = r'D:/otherSoft/chromeDriver/chromedriver84.0.4147.exe'

# 获取当前文件路径
current_path2 = inspect.getfile(inspect.currentframe())
PRO_PATH = os.path.dirname(current_path2) #当前项目的路径

