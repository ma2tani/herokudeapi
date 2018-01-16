# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
from datetime import datetime
import soclParseJson as spj

def bottomScroll(driver, scrollpage):
	data_list = [] # 全ページのデータを集める配列
	if isinstance( scrollpage,int ):
		if 0 < scrollpage:
			lenOfPage2 = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			match=False
			print(u"start execute / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			pagecount = 0
			while(match==False):
				lastCount = lenOfPage2
				sleep(3)
				lenOfPage2 = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
				pagecount+=1
				print(scrollpage,pagecount,lenOfPage2,lastCount)
				if scrollpage==pagecount or lastCount==lenOfPage2:
					match=True
					print(u"here last page")
			
			print(u"end execute / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			data = driver.page_source.encode('utf-8')
			soup = BeautifulSoup(data,"lxml") # lxml形式にする
			sound_list = soup.find_all("li",class_="soundList__item") # サウンド単位で抽出
			print(str(len(sound_list)) + u"件")
			print(u"start parse / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			# f = open('./output.json', 'w')

			return spj.soclParseJson(sound_list)
		if 0 == scrollpage:
			lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			match=False
			print(u"start execute / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			while(match==False):
				lastCount = lenOfPage
				sleep(3)
				lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
				if lastCount==lenOfPage:
					match=True
					print(u"here last page")
            
			print(u"end execute / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			data = driver.page_source.encode('utf-8')
			soup = BeautifulSoup(data,"lxml")
			sound_list = soup.find_all("li",class_="soundList__item")
			print(str(len(sound_list)) + u"件")
			print(u"start parse / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			# f = open('./output.json', 'w')

			return spj.soclParseJson(sound_list)
