# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

def bottomScroll(driver, scrollpage):
	if isinstance( scrollpage,int ):
		if 0 == scrollpage:
			lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
			match=False
			while(match==False):
				lastCount = lenOfPage
				sleep(2)
				lenOfPage = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
				if lastCount==lenOfPage:
					match=True
		elif 0 < scrollpage: 
			for i in range(scrollpage):
				driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
				sleep(2)
