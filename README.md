# socl-tracks-api
https://herokusocl.herokuapp.com/

Get data list of sound cloud artist
```{DEPLOY_URL}/scrollPageNo/artistName/section```

## Example
```{DEPLOY_URL}/0/artistName/tracks```
scrollPageNo=0 get all tracks

## Heroku env
```
$ pip install flask
$ pip install flask_cors
$ pip install BeautifulSoup4
$ pip install gunicorn
$ pip install lxml
$ pip install configparser
$ pip freeze > requirements.txt

$ echo python-3.6.0 > runtime.txt

$ echo web: gunicorn api:app --log-file=- > Procfile
```

your heroku app deploy

## Local env
edit api.py
```
    # **** Heroku env ****
    #options.binary_location = '/app/.apt/usr/bin/google-chrome'
    
    # **** Local env only ****
    '/usr/local/bin/chromedriver', 
```

local running
```$ python api.py```

