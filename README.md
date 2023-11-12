# Middle East War Data Analysis Project
![image](https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/5494026b-468e-45c0-b12f-67cadb0bbf05)

- <b>Description</b>: This repo is a Fatalities in the Israeli-Palestinian Data Analysis Project. (Middle East War)


### Data Description
|#|Column Name|Description|Missing Value|
|--|--|--|--|
|0|name|사망자 이름|-|
|1|date_of_event|사건 일자|-|
|2|age|사망자 나이|exist|
|3|citizenship|국적|-|
|4|event_location|사건 장소|-|
|5|event_location_district|사건 장소 지구|-|
|6|event_location_region|사건 장소 지역|-|
|7|date_of_death|사망 일자|-|
|8|gender|성별|exist|
|9|took_part_in_the_hostilities|교전 참가 여부|exist|
|10|place_of_residence|거주지|exist|
|11|place_of_residence_district|거주지 지구|exist|
|12|type_of_injury|부상 종류|exist|
|13|ammunition|탄약 종류|exist|
|14|killed_by|살해자|-|
|15|notes|사망 원인|exist|

### Schedule
|date|objective|status|
|:--:|:--:|:--:|
|23.10.28 ~ 23.11.03|Plan this project|O|
|23.11.04 ~ 23.11.10|Data Acquisition and Understand acquired data|O|
|23.11.11 ~ 23.11.11|Write Worksheets|O|
|23.11.12 ~ 23.11.12|Data Preprocessing|O|
|23.11.13 ~ 23.11.24|Data Visualization|in progress|
|23.11.25 ~ 23.12.01|Configuring the Streamlit Dashboard|-|
|23.12.02 ~ 23.12.08|Finish Project / Prepare a presentation|-|

### My Approach
- <b>Step1. Understand Data</b>
  |df.head().T|df.info()|df.isna().sum()|
  |:--:|:--:|:--:|
  |<img width="979" alt="스크린샷 2023-11-10 오전 12 32 04" src="https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/7e14ccb9-f518-413b-b845-5d756a6a473e">|<img width="498" alt="스크린샷 2023-11-10 오전 12 31 49" src="https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/cb7f6f09-5046-47ca-9f78-ad821642a69a">|<img width="317" alt="스크린샷 2023-11-10 오전 12 32 23" src="https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/84bf8ced-18dd-499e-9e8b-e3ab5c4b19b7">|
  
- <b>Step2. How to preprocess missing value</b>
  - age는 평균값으로 대체
  - gender, place_of_residence, place_of_residence_district, type_of_injury, note는 최빈값으로 대체
  - took_part_in_the_hostilities, ammunition은 변수 자체를 제거
 
- <b>Step3. Write Worksheets</b>
  |No|Question|
  |:--:|:--|
  |1|어느 국가에서 더 많이 사망하였을까?|
  |2|가장 많은 사상자가 발생한 연도가 언제일까?|
  |3|2014년에 사망자가 많이 발생한 지역 TOP3는 어디인가?|
  |4|2000년부터 2023년까지 일반적으로 어느 지역에서 가장 많은 사망자가 발생했을까?|
  |5|지도를 이용하여 사망자가 발생한 주요 지역을 시각화하면 어떨까?|
  |6|사망자들의 부상 종류 Top3는 무엇일까?|
  |7|성별과 나이별 사망자 수는 어떻게 될까?|

- <b>Step4. Data Preprocessing</b>

- <b>Step5. Data Visualization</b>
  
### Work Records
|date|main work|
|:--:|:--|
|23.10.20(Fri)|I created this repo.|
|23.11.08(Wed)|I acquired datasets in kaggle.|
|23.11.09(Thu)|I preprocessed missing values to a variety of methods(ex: replace NaN to mean value).<br>I visualized some data.|
|23.11.11(Sat)|I wrote worksheets.|
|23.11.12(Sun)|I preprocessed missing values.|

### References
[1] Dataset: https://www.kaggle.com/datasets/willianoliveiragibin/fatalities-in-the-israeli-palestinian/
