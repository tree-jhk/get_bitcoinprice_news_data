# **Bitcoin Dataset Generator and Bitcoin Datasets**

## **Introduction**
두 가지 폴더가 있습니다.  
>### **dataset_generator 폴더:**  
>- **get_bitcoin_news_data.py**  
비트코인 뉴스 데이터를 토큰화 과정을 거치고 불용어를 제거하는 코드입니다.  
텍스트 데이터만 수집할 때 사용하는 코드입니다.
>
>- **get_bitcoin_news_price_sentiment.ipynb**  
비트코인 뉴스 제목 데이터를 날짜별로 비트코인 OHLCV(시가,고가,저가,종가,거래량) 그리고 그 뉴스 제목 데이터의 감정 데이터를 저장하는 코드입니다.  
추가적으로, 위에서 만든 데이터의 하루동안의 모든 뉴스 데이터의 감정 값의 평균을 저장해서 간추린 데이터셋을 만드는 코드도 포함되어 있습니다.  
코드 내부에 사용법에 대한 주석을 달았습니다.  
   
>### **dataset 폴더:**
>- **Bitcoin_News_Sentiment_Data.csv**  
하루동안의 모든 뉴스 데이터의 감정 값의 평균을 저장해서 간추린 데이터셋을 만드는 코드도 포함되어 있습니다.  
데이터셋에 대한 자세한 정보:  
https://dynamic-tangelo-4e4.notion.site/Making-Dataset-Dataset-2-Bitcoin_News_sentiment_data-csv-cleaned-c0e918ffe8f9448ab755e5bbe5c125ff  
>
>
>- **Bitcoin_News_Title_Upbit_Price_Sentiment.csv**  
비트코인 뉴스 제목 데이터를 날짜별로 비트코인 OHLCV(시가,고가,저가,종가,거래량) 그리고 그 뉴스 제목 데이터의 감정 데이터를 저장한 데이터셋입니다.  
데이터셋에 대한 자세한 정보:  
https://dynamic-tangelo-4e4.notion.site/Making-Dataset-Dataset-1-Bitcoin_News_Title_Upbit_Price_Sentiment-csv-raw-27568dd480ef49e2867df798f6089fee


## **코드 만든 과정:**
https://velog.io/@tree_jhk/%EB%89%B4%EC%8A%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91-%EB%B0%8F-%EC%A0%84%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0-1-%EC%88%98%EC%A7%91%ED%95%98%EA%B8%B0