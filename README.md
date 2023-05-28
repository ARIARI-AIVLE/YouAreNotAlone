# 🥰 YouAreNotAlone : 사이버 폭력 근절을 위한 단계적 예방 전략 제안
2023년 공공데이터 기반 청소년상담복지사업 국민 아이디어 공모전 (대상 - 여성가족부 장관상)

<br>

## **💡 추진 배경 및 목적**
### 추진 배경
- 방송통신위원회의 보고에 따르면, 매년 사이버 폭력 피해와 가해가 증가하고 있음
- 한국인터넷진흥원에 따르면, 매년 청소년의 인터넷 사용시간과 활용 목적의 종류가 다양해지고 있음
- 그럼에도 불구하고 사이버 폭력에 대한 인식이 부족하므로 예방 교육 및 사업 확대의 필요성이 요구됨

### 목적
- Gerald Kaplan의 1,2,3차 예방 프레임워크를 바탕으로 각 단계에서의 사이버 폭력 예방 방안을 제안하여 사이버 폭력 문제 해결에 기여하고자 함
<br>

## **📌 프로젝트 개요**
<img src='https://github.com/ARIARI-AIVLE/YouAreNotAlone/assets/55778040/779ea4cd-ff5b-4e65-b96f-3699c01643f5'>

<br>
<br>

## **📝 프로젝트 세부 내용**
### [1차 예방]
- '2021년 한국지능정보사회진흥원 사이버폭력 실태조사 데이터' 활용 : 사이버 폭력 피해 청소년의 신고 인식 분석
- '2020년 청소년 매체 이용 및 유해환경 실태조사 데이터' 활용 : 성인용 컨텐츠 노출로 인한 피해 예방 교육 여부 분석

### [2차 예방]
- '2021년 한국지능정보사회진흥원 사이버폭력 실태조사 데이터' 활용
- 사이버 폭력 가해 청소년 분류 모델링 및 중요 특성 추출: Catboost와 SHAP 이용

### [3차 예방 : 사이버 폭력 상담 챗봇]
- 데이터 수집 및 전처리
   - 네이버 지식인 Q&A 데이터 크롤링, AI hub 감성 대화 말뭉치 수집 후 전처리
- 챗봇 학습
   - Ko-gpt2 : 질문에 대한 답변 생성
   - SentenceBERT : 매끄러운 답변을 위해 유사한 문장 제외
- 서비스 구현
   - Streamlit과 AWS EC2를 이용한 챗봇 웹사이트 구현

<br>

## **💌 활용 방안**
- 1차 예방 : 데이터 분석을 통한 사이버 폭력 예방을 위한 교육 전략
  - 사이버 폭력 신고 인식 교육 집중 개선
  - 유해 컨텐츠 노출 피해 예방 교육 확대
- 2차 예방 : 가해 청소년 분류 모델을 이용한 가해 청소년 조기 발굴 및 모니터링
  - Catboost를 이용한 예측 모델 활용
- 3차 예방 : 사이버 폭력 피해 학생들을 상담해주는 챗봇

<br>

## **✨ 기대효과**
- 1차 예방 : 기존보다 더 적은 예방교육 이수시간으로 보다 효과적이고 효율적인 예방 교육 가능
- 2차 예방 : 학교 폭력 위험군의 특성 파악 및 지도 방향 제시
- 3차 예방 : 청소년 사이버폭력 관련 상담의 질적 제고 기대
  - 청소년들은 민감한 주제인 사이버폭력 문의에 대한 부담 감소
  - 상담사들은 기초적인 상담은 인공지능 상담챗봇에 맡기고, 보다 상세하고 전문적인 상담에 집중할 수 있게 됨

<br>

## **👩‍🦰 팀원 및 역할 분담**
<table>
  <tr>
    <td align="center"><a href="https://github.com/bokkuembab"><img src="https://avatars.githubusercontent.com/u/88229105?v=4" width="100px;"><br /><sub><b>위예진</b></sub></td>
    <td align="center"><a href="https://github.com/heewon00" width="125" height="170"><img src="https://avatars.githubusercontent.com/u/55778040?v=4" width="100px;"><br /><sub><b>박희원</b></sub></td>
    <td align="center"><a href="https://github.com/jjhh0210"><img src="https://avatars.githubusercontent.com/u/85385027?v=4" width="100px;"><br /><sub><b>박지현</b></sub></td>
    <td align="center"><a href="https://github.com/lwy210"><img src="https://avatars.githubusercontent.com/u/33020581?v=4" width="100px;"><br /><sub><b>이원영</b></sub></td>
  </tr>
   <tr>
     <td align="center">👧🏻 위예진 <br> (팀장 : 데이터 분석, 모델링)</td>
     <td align="center">👧🏻 박희원 <br> (팀원 : 데이터 분석, 챗봇)</td>
     <td align="center">👧🏻 박지현 <br> (팀원 : 데이터 분석, 모델링)</td>
     <td align="center">👧🏻 이원영 <br> (팀원 : 데이터 분석, 모델링)</td>
 </tr>
</table>

<br>

## **🔧 기술 스택**
<div>
  <img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"> 
  <img src="https://img.shields.io/badge/keras-D00000?style=for-the-badge&logo=keras&logoColor=white">
  <img src="https://img.shields.io/badge/Google Colab-F9AB00?style=for-the-badge&logo=Google Colab&logoColor=white">
  <img src="https://img.shields.io/badge/git-F05032?style=for-the-badge&logo=git&logoColor=white">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white">
  <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white">
 </div>
