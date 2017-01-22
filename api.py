# -*- coding: utf-8 -*-

import json
# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver 
from selenium.webdriver.common.keys import Keys # 文字を入力する時に使う
import bottomScroll as bosc

#ここからflaskの必要分
import os
from flask import Flask

import configparser
setparam = configparser.SafeConfigParser()
setparam.read(os.path.abspath(os.path.dirname(__file__))+'/socl_settings.py')

#ここからflaskでcorsの設定 ajaxを使う時のクロスドメイン制約用
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "使い方 : /api/ページ数/アーティスト名/セクション"

@app.route('/api/<int:page>/<string:artist>/<string:sect>') # ページ数/アーティスト/検索場所をパスから変数に受け取る
def sound(page,artist,sect):
 
    driver = webdriver.PhantomJS() # PhantomJSを使う 
    #driver = webdriver()
    #exec(setparam.get('settings', 'set_driver'), globals(), driver)
    driver.set_window_size(int(setparam.get('settings', 'window_w')), int(setparam.get('settings', 'window_h'))) # PhantomJSのサイズを指定する
    driver.implicitly_wait(int(setparam.get('settings', 'driver_wait'))) # 指定した要素などがなかった場合出てくるまでdriverが最大20秒まで自動待機してくれる

    URL = "https://soundcloud.com/"+str(artist)+"/"+str(sect)
    driver.get(URL) # slideshareのURLにアクセスする
    #driver.get(setparam.get('settings', 'URL')+str(artist)+str(sect)) # slideshareのURLにアクセスする
    
    data_list = [] # 全ページのデータを集める配列
    data_list = (bosc.bottomScroll(driver, page))

    driver.close() # ブラウザ操作を終わらせる
    jsonstring = json.dumps(data_list,ensure_ascii=False,indent=int(setparam.get('settings', 'json_indent'))) # 作った配列をjson形式にして出力する
    return jsonstring
 
# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
