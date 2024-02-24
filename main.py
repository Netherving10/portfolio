import streamlit


CONTENT_1 = '''
1. "Венец победы воина - это смирение перед своими врагами."
2. "Нет ничего более могущественного, чем идея, рожденная в свое время."
3. "Мудрость не заключается в том, чтобы знать все, а в том, чтобы понимать, что нужно знать."
'''
CONTENT_2 = "Below yo can find some of the apps I have built in Python. Feel free to contact me!"

streamlit.set_page_config(layout="wide")
col1, col2 = streamlit.columns(2)

with col1:
    streamlit.image("dru.jpg")

with col2:
    streamlit.title("Netherving")
    streamlit.info(CONTENT_1)

streamlit.write(CONTENT_2)