# -*- coding: utf-8 -*-

# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys # 文字を入力する時に使う
from time import sleep

def bottomScroll(driver, scrollpage):
	data_list = [] # 全ページのデータを集める配列
	if isinstance( scrollpage,int ):
		if 0 == scrollpage:
			lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			match=False
			while(match==False):
				lastCount = lenOfPage
				sleep(3)
				lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
				if lastCount==lenOfPage:
					match=True
            
			data = driver.page_source.encode('utf-8')
			soup = BeautifulSoup(data,"lxml") # 加工しやすいようにlxml形式にする
			sound_list = soup.find_all("li",class_="soundList__item") # サウンド単位で抽出
			print(str(len(sound_list)) + u"件")
			for sound in sound_list:
				sound_in = {} # サウンドの情報を辞書形式でまとめる
                
				# サウンドの投稿者の名前を入手
				name = sound.find("span",class_="soundTitle__usernameText").text
				#print(str(name))
				sound_in["name"] = name.strip() # strip()は両端の空白と改行をなくしてくれる
                
				# サウンドのタイトルを入手
				title = sound.find("a",class_="soundTitle__title").find("span").text
				#title = titles.find("span").text_content()
				#print(str(title).encode('utf-8'))
				# 指定したタグ&クラス内のtitleを出す
				sound_in["title"] = title.strip()
                
				# サウンドのリンクを入手
				link = sound.find("a",class_="soundTitle__title").get("href")
				# 指定したタグ&クラス内のhrefを出す
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
				plays = sound.find("li", class_="sc-ministats-item").get("title")
				#print(str(plays))
				sound_in["plays"] = plays

				# サウンドのイメージ
				imagetag = sound.find("span",class_="image__full").get("style")
				image = imagetag[imagetag.find("url(")+4:imagetag.find(");")]
				sound_in["image"] = image
                
				data_list.append(sound_in) # data_listに1ページ分の内容をまとめる

			return data_list

