# coding:utf-8
# __author__ : 'Bo_lin Chen'
# Date : 2019/6/6


import time
from selenium import webdriver


options = webdriver.ChromeOptions()

options.binary_location = "/Applications/海龟编辑器.app/Contents/MacOS/海龟编辑器"

wood_win = webdriver.Chrome(options=options)
time.sleep(4)

# wood_win.quit()