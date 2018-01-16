# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 文字を入力する時に使う
from selenium.webdriver.chrome.options import Options
from time import sleep
import json
from datetime import datetime

def soclParseJson(sound_list):
    data_list = [] 
    for sound in sound_list:
        sound_in = {} # サウンドの情報を辞書形式でまとめる
        
        # サウンドの投稿者の名前を入手
        name = sound.find("span",class_="soundTitle__usernameText").text
        # print(str(name))
        sound_in["name"] = name.strip() # strip()は両端の空白と改行をなくしてくれる
        
        # サウンドのタイトルを入手
        title = sound.find("a",class_="soundTitle__title").find("span").text
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
        if sound.find("li", class_="sc-ministats-item"):
            plays = sound.find("li", class_="sc-ministats-item").get("title")

            sound_in["plays"] = plays
        else:
            sound_in["plays"] = u"0 plays"

        # サウンドのイメージ
        imagetag = sound.find("span",class_="image__full").get("style")
        image = imagetag[imagetag.find("url(")+4:imagetag.find(");")]
        sound_in["image"] = image
        
        # data_list =sound_in # data_listに1ページ分の内容をまとめる
        data_list.append(sound_in)
        # f.write(str(sound_in))

    return data_list
