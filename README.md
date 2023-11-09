# Middle East War Data Analysis Project
- <b>Description</b>: This repo is a Fatalities in the Israeli-Palestinian Data Analysis Project. (Middle East War)
![image](https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/5494026b-468e-45c0-b12f-67cadb0bbf05)

### Data Description
<img width="360" alt="스크린샷 2023-11-10 오전 12 31 32" src="https://github.com/PSLeon24/Israeli-Palestinian_Data_Analysis_Project/assets/59058869/79f0dfd0-5f15-4b62-aeb2-2ba3d71e4343">

### Schedule
|date|objective|status|
|:--:|:--:|:--:|
|23.10.28 ~ 23.11.03|Plan this project|O|
|23.11.04 ~ 23.11.10|Data Acquisition and Understand acquired data|O|
|23.11.11 ~ 23.11.12|Write Worksheets|in progress|
|23.11.13 ~ 23.11.14|Data Preprocessing|-|
|23.11.15 ~ 23.11.24|Data Visualization|-|
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
  |3|To be added|

- <b>Step4. Data Preprocessing</b>

- <b>Step5. Data Visualization</b>
  
### Work Records
|date|main work|
|:--:|:--|
|23.10.20(Fri)|I created this repo.|
|23.11.08(Wed)|I acquired datasets in kaggle.|
|23.11.09(Thu)|I preprocessed missing values to a variety of methods(ex: replace NaN to mean value).<br>I visualized some data.|

### References
[1] Dataset: https://www.kaggle.com/datasets/willianoliveiragibin/fatalities-in-the-israeli-palestinian/
