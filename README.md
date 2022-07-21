날짜별 비트코인 가격, 기사 제목을 수집하고,  
수집한 데이터에 BERT FinBERT를 이용한 감정 분석을 진행합니다.     
Collect bitcoin prices by date and article titles,
and conduct an emotional analysis using BERT FinBERT for the collected data.  

get_bitcoin_news_data.py:   
inveseting.com에서 기사 제목을 수집하고 날짜별로 정리해서 txt 파일에 저장하는 코드입니다.  
코드에 대한 자세한 설명은 아래에 있습니다.  
get_bitcoin_news_data.py:   
Code that collects article titles from inveseting.com, organizes them by date, and stores them in a txt file.  
A detailed description of the code is below.

https://velog.io/@tree_jhk/%EB%89%B4%EC%8A%A4-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%88%98%EC%A7%91-%EB%B0%8F-%EC%A0%84%EC%B2%98%EB%A6%AC%ED%95%98%EA%B8%B0-1-%EC%88%98%EC%A7%91%ED%95%98%EA%B8%B0

get_bitcoinprice_news_data.py:  
토큰화 과정을 거치고 불용어를 제거했습니다. 머신러닝으로 텍스트 데이터를 수집할 때는 전처리를 꼼꼼히 해야하기 때문에 추천합니다.


# FE News

<img src="./assets/logo.svg" width="150" align="right" style="margin:0 0 0 20px">

FE News는 네이버 FE 엔지니어들이 엄선한 양질의 `FE 및 주요한 기술 소식`들을 큐레이션 해 공유하는 것을 목표로 합니다.
이를 통해 국내 개발자들에게 지식 공유에 대한 가치 인식과 성장에 도움을 주고자 합니다. :grin:

> 네이버 Front-end 조직이 어떤 일을 하고, 개발자들이 어떻게 성장하고 있는지 궁금하신가요?<br>
>
> - [네이버 Front-end 소개](../../tree/fe-org)

## 🚩 발행소식

발행소식은 [`/issues`](/issues) 폴더 내의 `yyyy-mm.md` 파일을 통해 확인할 수 있습니다.

## 📆 발행주기

매월 첫째 주 수요일, 월 1회 발행

## 🔔 구독방법
다음의 2가지 방법을 통해 발행 소식을 구독하실 수 있습니다.
> [참고] 대부분의 커밋은 소식의 발행 또는 오타, 정보 수정에 대한 PR의 머지 수준에서 발생합니다.

- 프로젝트 `watch`를 통해 구독하기
  - 저장소 상단의 `watch` 버튼을 클릭해 프로젝트를 지켜보는 것으로 구독
- RSS 리더를 통해 구독하기
  - RSS 리더를 통해 프로젝트 커밋을 구독
    - https://github.com/naver/fe-news/commits/master.atom

## 📬 최신소식

> 이전 소식들은 '연도'를 클릭하면 보실 수 있습니다.
### 2022
- [2022-07](/issues/2022-07.md)
- [2022-06](/issues/2022-06.md)
- [2022-05](/issues/2022-05.md)
- [2022-04](/issues/2022-04.md)
- [2022-03](/issues/2022-03.md)
- [2022-02](/issues/2022-02.md)
- [2022-01](/issues/2022-01.md)

<details>
  <summary>2021</summary>

- [2021-12](/issues/2021-12.md)
- [2021-11](/issues/2021-11.md)
- [2021-10](/issues/2021-10.md)
- [2021-09](/issues/2021-09.md)
- [2021-08](/issues/2021-08.md)
- [2021-07](/issues/2021-07.md)
- [2021-06](/issues/2021-06.md)
- [2021-05](/issues/2021-05.md)
- [2021-04](/issues/2021-04.md)
- [2021-03](/issues/2021-03.md)
- [2021-02](/issues/2021-02.md)
- [2021-01](/issues/2021-01.md)
</details>
<details>
  <summary>2020</summary>

- [2020-12](/issues/2020-12.md)
- [2020-11](/issues/2020-11.md)
- [2020-10](/issues/2020-10.md)
- [2020-09](/issues/2020-09.md)
- [2020-08](/issues/2020-08.md)
- [2020-07](/issues/2020-07.md)
- [2020-06](/issues/2020-06.md)
- [2020-05](/issues/2020-05.md)
- [2020-04](/issues/2020-04.md)
- [2020-03](/issues/2020-03.md)
- [2020-02](/issues/2020-02.md)
</details>
