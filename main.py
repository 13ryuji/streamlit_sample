import streamlit as st
import pandas as pd
import numpy as np

biz_list = [
    'web制作',
    'SNS運用',
    'RPA'
]

achievement_list = [
    'https://ryuji-web-sample.web.app/',
]

bonz_list = [
    'http://test.kk-mark.com/',
    'http://demo.kanasashi-mcnet.com/',
    'https://demo2.kanasashi-mcnet.com/',
    'http://demo3.kanasashi-mcnet.com/',
]

seed_list = [
    'さわやかビッグデータプロジェクト',
    '地域メタゲーム集計ツール',
    'ローカル線めぐりパーフェクトガイド',
    '',
]
st.title('Maverick')
st.header('事業内容')
for i in biz_list:
    st.markdown('- ' + i)


st.header('実績')
for i in achievement_list:
    st.markdown('- ' + i)

st.subheader('ボンズ　デモサイト')
for i in bonz_list:
    st.markdown('- ' + i)

st.header('ネタ')
for i in seed_list:
    st.markdown('- ' + i)
