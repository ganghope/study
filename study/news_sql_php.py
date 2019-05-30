import requests
from bs4 import BeautifulSoup
import pymysql

# MySQL Connection 연결
conn = pymysql.connect(
    host = '54.180.142.13' ,
    user = '-' ,
    password = '-' ,
    db = '-',
    charset='utf8')
curs = conn.cursor() # Connection 으로부터 Cursor 생성

URL = 'https://www.boannews.com/media/o_list.asp' # 가장많이본기사
URL2 = 'https://www.boannews.com/media/s_list.asp?skind=5' #취약점 경고 및 버그리포트
URL3 = 'https://www.boannews.com/media/s_list.asp?skind=i' # 보안ㆍIT산업 동향
res = requests.get(URL) # get방식으로 html 요청후 저장
res2 = requests.get(URL2)
res3 = requests.get(URL3)
bsObject = BeautifulSoup(res.text, "html.parser")
bsObject2 = BeautifulSoup(res2.text, "html.parser")
bsObject3 = BeautifulSoup(res3.text, "html.parser")
news = bsObject.find("div", id="news_area") # 해당구역 html 추출 저장
bnews = bsObject2.find("div", id="news_area")
cnews = bsObject3.find("div", id="news_area")

# 1. 가장 많이본 기사 추출
news_title = [] # 기사 제목
href = [] # 기사 링크
date = [] # 기사 작성일자
for tag in news.find_all('span', class_='news_txt'):
    news_title.append(tag.string)  # 문자형으로 리스트에 추가
for tag in news.findAll("a"):
    href.append(tag.get('href')) # 속성 href 리스트에 추가
for i in range(0,20):
    del href[i] # href가 리스트에 두번씩 반복되어서 중복되는 href 제거
for tag in news.find_all('span', class_='news_writer'):
    date.append(tag.string) # 작성일자 추가

# 2. 취약점 경고 및 버그리포트 추출
news_title2 = []
href2 = []
date2 = []
for tag2 in bnews.find_all('span', class_='news_txt'):
    news_title2.append(tag2.string)
for tag2 in bnews.findAll("a"):
    href2.append(tag2.get('href'))
for i in range(0,20):
    del href2[i]
for tag2 in bnews.find_all('span', class_='news_writer'):
    date2.append(tag2.string)

# 3. 보안ㆍIT산업 동향
news_title3 = []
href3 = []
date3 = []
for tag3 in cnews.find_all('span', class_='news_txt'):
    news_title3.append(tag3.string)
for tag3 in cnews.findAll("a"):
    href3.append(tag3.get('href'))
for i in range(0,20):
    del href3[i]
for tag3 in cnews.find_all('span', class_='news_writer'):
    date3.append(tag3.string)

categ = ['가장 많이 본 기사', '취약점 경고 및 버그리포트', '보안ㆍIT산업 동향']

sql = 'INSERT INTO news_rank (category, news_title, link, writer) VALUES (%s, %s, %s, %s)'  # 데이터 삽입
sql2 = 'INSERT INTO news2 (category, news_title, link, writer) VALUES (%s, %s, %s, %s)' # 테이블 3개 생성해서 별도관리
sql3 = 'INSERT INTO news3 (category, news_title, link, writer) VALUES (%s, %s, %s, %s)'
for title, hr, wr in zip(news_title, href, date):
    curs.execute(sql, (categ[0], title, hr, wr)) # 기사 카테고리, 제목, 링크, 작성일자 순으로 db에 업로드
for title2, hr2, wr2 in zip(news_title2, href2, date2):
    curs.execute(sql2, (categ[1], title2, hr2, wr2))
for title3, hr3, wr3 in zip(news_title3, href3, date3):
    curs.execute(sql3, (categ[2], title3, hr3, wr3))
conn.commit() # 최종 저장
