# html 정보 가져오기 및 headers 세팅
headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}

def get_url_info(iter):
    if iter==1:
        url = "https://www.investing.com/crypto/bitcoin/news"
    else:
        url = f"https://www.investing.com/crypto/bitcoin/news/{iter}"
    response = requests.get(url,headers=headers)
    return BeautifulSoup(response.text,'lxml')

import requests
from bs4 import BeautifulSoup
import re

import sys
f = open('c:/Users/kjsjh/Desktop/nlp_preprocessing.txt','w',-1, 'utf-8')

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

import pyupbit
ticker = 'KRW-BTC'
interval = 'day'
to = '2022-05-01 09:00'
count = 30
upbit_info = pyupbit.get_ohlcv(ticker=ticker,interval=interval,to=to,count=count)

# 값을 저장할 데이터셋을 딕셔너리형으로 받는다.
news_date_title_dictionary = {}

# 종료시키는 finish bool형 변수
finish=False

# 불용어 list 생성
remove = 'q w e r t y u i o p a s d f g h j k l z x c v b n m '.split() + stopwords.words('english')

for iter in range(33,1000):
    soup = get_url_info(iter)
    news_title_list, news_date_list=[], []
    for i,title in enumerate(soup.select(".title")):
        title_string = title.get('title')
        if title_string!=None and i>=14:
            # 전처리 소문자화, 특수문자 제거, 불용어 제거
            title_string = title_string.lower()
            title_string = re.sub('[-=+,#/\??:^.@*\"※~ㆍ!』‘|\(–ه\)\[\]—`\…》’\”\“\’·$’|/“%]|[0-9]',' ',title_string).strip().split()
            for r in remove:
                if r in title_string:
                    title_string.remove(r)
            news_title_list.append(title_string)
    for date in soup.select(".date"):
        date_string = date.get_text()
        if "Apr" in date_string:
            news_date_list.append(date_string[3:])
        elif "Mar" in date_string:
            finish = True
    for date, title in zip(news_date_list, news_title_list):
        if date in news_date_title_dictionary:
            # 마지막 날짜의 바로 전날의 날짜가 news_date_list에 있으면 종료한다.
            news_date_title_dictionary[date].append(title)
        else:
            news_date_title_dictionary[date]=[title]
    if finish:
        break
for date,title in news_date_title_dictionary.items():
    title.append(upbit_info.loc["2022-04-01 09:00:00+09:00":"2022-04-30 09:00:00+09:00"]['close'][int(date[4:6])-1])
    f.write(f"기사 작성 날짜:{date}\n기사 제목들:{title}\n\n")
    # print(f"기사 작성 날짜:{date}\n기사 제목들:{title}\n",file=f,encoding='UTF-8')
f.close