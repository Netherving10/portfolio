import streamlit as st
import pandas


CONTENT_1 = '''
1. "Венец победы воина - это смирение перед своими врагами."
2. "Нет ничего более могущественного, чем идея, рожденная в свое время."
3. "Мудрость не заключается в том, чтобы знать все, а в том, чтобы понимать, что нужно знать."
'''
CONTENT_2 = "Below yo can find some of the apps I have built in Python. Feel free to contact me!"

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("dru.jpg")

with col2:
    st.title("Netherving")
    st.info(CONTENT_1)

st.write(CONTENT_2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Souce code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Souce code]({row['url']})")
