# -*- coding: utf-8 -*-
# 日本語を使う場合は絶対に必要

# flaskなどの必要なライブラリをインポート
import os
from flask import Flask

# 自分の名称を app という名前でインスタンス化
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

# bashで叩いたかimportで入れたかを判定する
if __name__ == '__main__':
    app.run()
