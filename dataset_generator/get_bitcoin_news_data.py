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
import pandas

def get_news_data_with_date(page_number:int,first_date:str,exculde_date:str):
    date_error = '\nERROR: Date is not in proper form.\n'
    month = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    if first_date[:3] not in month or exculde_date[:3] not in month:
        print(date_error)
        return {}
    elif len(first_date) != 12 or first_date[3] != ' ' or first_date[6:8] != ', ' or len(exculde_date) != 12 or exculde_date[3] != ' ' or exculde_date[6:8] != ', ':
        print(date_error)
        return {}
    
    finish=False
    news_date_title_dictionary = {}

    for page_num in range(page_number,9999999999):
        soup = get_url_info(page_num)
        news_title_list, news_date_list=[], []
        for i,title in enumerate(soup.select(".title")):
            title_string = title.get('title')
            if title_string != None:
                news_title_list.append(title_string)
            print(title_string)
        for date in soup.select(".date"):
            date_string = str(date.get_text())
            if exculde_date != date_string[3:]:
                if (first_date) == date_string[3:]:
                    finish = True
                else:
                    news_date_list.append(date_string)
            
        for date, title in zip(news_date_list, news_title_list):
            if date in news_date_title_dictionary:
                news_date_title_dictionary[date].append(title)
            else:
                news_date_title_dictionary[date]=[title]
        if finish:
            break
    return news_date_title_dictionary

news_date_title_dictionary = get_news_data_with_date(18,'Jun 13, 2022','Jun 16, 2022')

# 감정 분석

f = open('nlp_preprocessing.txt','w',-1, 'utf-8')
for date,title in news_date_title_dictionary.items():
    f.write(f"기사 작성 날짜:{date}\n기사 제목들:{title}\n\n")
f.close