# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import json
from datetime import datetime

def bottomScroll(driver, scrollpage):
	data_list = [] # 全ページのデータを集める配列
	if isinstance( scrollpage,int ):
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
			soup = BeautifulSoup(data,"lxml") # lxml形式にする
			sound_list = soup.find_all("li",class_="soundList__item") # サウンド単位で抽出
			print(str(len(sound_list)) + u"件")
			print(u"start parse / "+datetime.now().strftime("%Y/%m/%d %H:%M:%S"))
			# f = open('./output.json', 'w')
			for sound in sound_list:
				sound_in = {} # サウンドの情報を辞書形式でまとめる
                
				# サウンドの投稿者の名前を入手
				name = sound.find("span",class_="soundTitle__usernameText").text
				# print(str(name))
				sound_in["name"] = name.strip()
                
				# サウンドのタイトルを入手
				title = sound.find("a",class_="soundTitle__title").find("span").text
				#print(str(title).encode('utf-8'))
				sound_in["title"] = title.strip()
                
				# サウンドのリンクを入手
				link = sound.find("a",class_="soundTitle__title").get("href")
				#print(str(link))
				sound_in["link"] = "https://soundcloud.com" + link
                
				# 投稿日時
				uploadTime = sound.find("time").get("datetime")
				#print(str(uploadTime))
				sound_in["uploadTime"] = uploadTime.strip()
                
				# 投稿経過時間
				postedTime = sound.find("time").get("title")
				#print(str(postedTime))
				sound_in["postedTime"] = postedTime.strip()
                
				# 再生回数
				if sound.find("li", class_="sc-ministats-item"):
					plays = sound.find("li", class_="sc-ministats-item").get("title")

					sound_in["plays"] = plays
				else:
					sound_in["plays"] = u"0 plays"

				# サウンドのイメージ
				imagetag = sound.find("span",class_="image__full").get("style")
				image = imagetag[imagetag.find("url(")+4:imagetag.find(");")]
				sound_in["image"] = image
                
				# data_listに1ページ分の内容をまとめる
				data_list.append(sound_in)
				# f.write(str(sound_in))

			return data_list

