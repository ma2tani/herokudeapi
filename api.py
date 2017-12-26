# -*- coding: utf-8 -*-

import json
# ここからスクレイピング必要分
from bs4 import BeautifulSoup
# ここからseleniumでブラウザ操作必要分
from selenium import webdriver
from selenium.webdriver.common.keys import Keys  # 文字を入力する時に使う
from selenium.webdriver.chrome.options import Options
import bottomScroll as bosc

# ここからflaskの必要分
import os
from flask import Flask

import configparser
setparam = configparser.SafeConfigParser()
setparam.read(os.path.abspath(os.path.dirname(__file__)) + '/socl_settings.py')

# ここからflaskでcorsの設定 ajaxを使う時のクロスドメイン制約用
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app)


@app.route('/')
def index():
    return "使い方 : /api/ページ数/アーティスト名/セクション"


# ページ数/アーティスト/検索場所をパスから変数に受け取る
@app.route('/api/<int:page>/<string:artist>/<string:sect>')
def sound(page, artist, sect):

    # driver = webdriver.PhantomJS() # PhantomJSを使う
    options = webdriver.ChromeOptions()
    # 必須
    options.add_argument('--headless')
    # options.add_argument('--disable-gpu')
    # エラーの許容
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--disable-web-security')
    # headlessでは不要そうな機能
    options.add_argument('--disable-desktop-notifications')
    options.add_argument("--disable-extensions")

    # 言語
    options.add_argument('--lang=ja')
    # 画像を読み込まないで軽くする
    options.add_argument('--blink-settings=imagesEnabled=false')

    # options.add_argument('remote-debugging-port=9222')
    # options.add_argument('disable-gpu')
    # options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(
        '/usr/local/bin/chromedriver', chrome_options=options)

    #driver = webdriver()
    #exec(setparam.get('settings', 'set_driver'), globals(), driver)
    # driver.set_window_size(int(setparam.get('settings', 'window_w')), int(setparam.get('settings', 'window_h'))) # PhantomJSのサイズを指定する
    # 指定した要素などがなかった場合出てくるまでdriverが最大20秒まで自動待機してくれる
    driver.implicitly_wait(int(setparam.get('settings', 'driver_wait')))

    URL = "https://soundcloud.com/" + str(artist) + "/" + str(sect)
    driver.get(URL)  # URLにアクセスする
    # driver.get(setparam.get('settings', 'URL')+str(artist)+str(sect)) # のURLにアクセスする

    data_list = []  # 全ページのデータを集める配列
    data_list = (bosc.bottomScroll(driver, page))

    driver.close()  # ブラウザ操作を終わらせる
    driver.quit()
    jsonstring = json.dumps(data_list, ensure_ascii=False, indent=int(
        setparam.get('settings', 'json_indent')))  # 作った配列をjson形式にして出力する
    return jsonstring


# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
