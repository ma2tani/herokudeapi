# -*- coding: utf-8 -*-

import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import bottomScroll as bosc
import soclParseJson as spj

import os
from flask import Flask

import configparser
setparam = configparser.SafeConfigParser()
setparam.read(os.path.abspath(os.path.dirname(__file__)) + '/socl_settings.py')

from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "使い方 : /api/pageNo/ArtistName/section"


# ページ数/アーティスト/検索場所をパスから変数に受け取る
@app.route('/api/<int:page>/<string:artist>/<string:sect>')
def sound(page, artist, sect):

    options = webdriver.ChromeOptions()
    
    # **** Heroku env only ****
    options.binary_location = '/app/.apt/usr/bin/google-chrome'
    
    options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    options.add_argument('--disable-desktop-notifications')
    options.add_argument("--disable-extensions")

    # 言語
    options.add_argument('--lang=ja')
    # 画像を読み込まない
    options.add_argument('--blink-settings=imagesEnabled=false')

    driver = webdriver.Chrome(
    # **** Local env only ****
    # '/usr/local/bin/chromedriver', 
    chrome_options=options)
    

    driver.implicitly_wait(int(setparam.get('settings', 'driver_wait')))

    URL = "https://soundcloud.com/" + str(artist) + "/" + str(sect)
    driver.get(URL)  # URLにアクセスする

    data_list = []  # 全ページのデータを集める配列
    data_list = (bosc.bottomScroll(driver, page))

    driver.close()
    driver.quit()
    jsonstring = json.dumps(data_list, ensure_ascii=False, indent=int(
        setparam.get('settings', 'json_indent')))  # 作った配列をjson形式にして出力する
    return jsonstring


# shで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
