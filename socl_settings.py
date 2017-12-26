[settings]
window_w : 1024
window_h : 850
driver_wait : 20
URL : https://soundcloud.com/
set_driver : webdriver.PhantomJS()
# options : webdriver.ChromeOptions().add_argument('--headless').add_argument('--disable-gpu').add_argument('disable-gpu')add_argument('--ignore-certificate-errors').add_argument('--allow-running-insecure-content').add_argument('--disable-web-security').add_argument('--disable-desktop-notifications').add_argument("--disable-extensions").add_argument('--lang=ja').add_argument('--blink-settings=imagesEnabled=false').add_argument('remote-debugging-port=9222').add_argument('--no-sandbox')
# set_driver : webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=options)
# driver.get('hogehoge.com')
search_box_element : nav-search-query
json_indent : 2
