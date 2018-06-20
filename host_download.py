#!/usr/local/bin/python3

import requests
from bs4 import BeautifulSoup
import bs4
import re
import zipfile

# pip install requests
# pip install beautifulsoup4

def getHtml(url):
	try:
		r = requests.get(url)
		r.raise_for_status
		r.encoding = r.apparent_encoding
		return r.text
	except Exception as e:
		raise e

def getHtmlTitle(html):
	soup = BeautifulSoup(html,"html.parser")
	return soup.title

def getPwd(html):
	soup = BeautifulSoup(html,"html.parser")
	links = soup.find_all('span')
	pwd = ""  
	for link in links:
		if "百度网盘" in link.get_text() :
			print(link.get_text())
			pwd = link.get_text()
			list = pwd.split("：")
			pwd = list[1]
			print(pwd)
			break
	return pwd

def getTitleDate(title):
	num = re.search( r'2018-\d\d-\d\d',title.string)
	date = num.group()
	print("最新更新日期为："+date)
	return re.sub(r'\D', "", date)

def getFileName(downloadHtml):
	soup = BeautifulSoup(downloadHtml,"html.parser")
	links = soup.find_all('a')  
	# for link in links:      
	# 	print (link.name,link['href'],link.get_text()  )  
	# print(links[2]['href'])
	return links[2]['href']

def downLoad(downloadUrl,date):
	print(downloadUrl)
	r = requests.get(downloadUrl)
	with open("hosts"+date+".zip", "wb") as code:
		code.write(r.content)

def extract(name,pwd):
	f = zipfile.ZipFile(name, 'r')
	for file in f.namelist():
		f.extract(file,".",str.encode(pwd))#b"google" ，密码需为byte格式

def main():
	url = "https://laod.cn/hosts/2018-google-hosts.html"
	serverUrl = "https://iiio.io/download/"

	html = getHtml(url)
	title = getHtmlTitle(html)

	date = getTitleDate(title)
	serverHtml = getHtml(serverUrl + date)
	print(serverUrl + date)

	fileName = getFileName(serverHtml)
	downloadUrl = serverUrl+date+'/'+fileName

	downLoad(downloadUrl,date)
	print("下载完成")
	
	pwd = getPwd(html)

	extract("hosts"+date+".zip",pwd)

	print("任务完成")
	

main()

