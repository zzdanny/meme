#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup

def fix(string):
	return string.replace(" ", "").replace("\n", "").replace("\t", "")

zodizc = ['白羊座', '金牛座', '雙子座', '巨蟹座', '獅子座', '處女座', '天秤座', '天蝎座' ,'射手座' ,'摩羯座' ,'水瓶座' ,'雙魚座']
content = []
url = 'http://fate.ximizi.com/peidui_aiqing.php'

for B in zodizc:
	for G in zodizc:
		url = 'http://fate.ximizi.com/peidui_aiqing.php'
		response = requests.post(url, data = {'B': '白羊座', 'G': '天秤座'})
		html = response.content
		soup = BeautifulSoup(html, 'html.parser')
		content = soup.findAll('p')
		for index, p in enumerate(content):
			if index in(1, 3, 5, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17):
				if fix(p.text) != '':
					print fix(p.text)
		print