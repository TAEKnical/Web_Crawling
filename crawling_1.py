import requests
from bs4 import BeautifulSoup as bs

#!) requests 라이브러리를 활용한 HTML 페이지 요청
#1-1) res 객체에 HTML 데이터갖 ㅓ장되고, res.content로 데이터를 추출할 수 있음.
res=requests.get("https://sports.news.naver.com/wfootball/news/read.nhn?oid=139&aid=0002096638")

# print(res.content)

#2) HTML 페이지 파싱 BeautifulSoup(Html데이터, 파싱방법)
#2-1) BeautifulSoup 파싱방법
soup = bs(res.text,'html.parser')

#3) 필요한 데이터 검색
title=  soup.find('title')

#4) 필요한 데이터 추출
print(title.get_text())