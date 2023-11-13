import streamlit as st

st.header("Middle East War Data Analysis Project")
st.subheader("a Fatalities in the Israeli-Palestinian")

questions = [
    "어느 국가에서 더 많이 사망하였을까?",
    "가장 많은 사상자가 발생한 연도가 언제일까?",
    "2014년에 사망자가 많이 발생한 지역 TOP3는 어디인가?",
    "2000년부터 2023년까지 일반적으로 어느 지역에서 가장 많은 사망자가 발생했을까?",
    "지도를 이용하여 사망자가 발생한 주요 지역을 시각화하면 어떨까?",
    "사망자들의 부상 종류 Top3는 무엇일까?",
    "성별과 나이별 사망자 수는 어떻게 될까?",
]

st.sidebar.title("Question")
select_species = st.sidebar.selectbox("확인하고 싶은 질문을 선택하세요.", questions)
st.sidebar.text("Made by Yeongmin Ko")
