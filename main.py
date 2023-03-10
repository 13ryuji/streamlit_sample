import streamlit as st
import pandas as pd
import numpy as np

biz_list = [
    'アンケート作成&集計',
    'RPA',
    '動画制作',
    'SNS運用',
    'web制作',
]

achievement_list = [
    'https://13ryuji-mtg-limited-balance-app-yn7767.streamlit.app/',
    'https://ryuji-web-sample.web.app/',
    'https://lookerstudio.google.com/u/0/reporting/f64eb01b-92d8-42a0-b4bf-116d3bd2395e/page/7OeBD',
    'https://lookerstudio.google.com/u/0/reporting/fe94d0b9-2997-435a-8178-b68e3092ca4d/page/esp6C',
    'https://docs.google.com/forms/d/e/1FAIpQLSdLjVrNiLXZ_GOnqe-BpfOaRzOdUBy0F3ztM9tGsBrLDT4qAA/viewform',
    'https://youtu.be/cQ3za3qn9fw',
    'https://youtu.be/Iv_moPO-k7c',
    'https://youtu.be/v-ko11CcRJE',
    'https://youtu.be/1s9POUTwh0E',
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
    'アリーナコード一発コピペ',
    'ローカル線めぐりパーフェクトガイド',
    '商工会のプロと学ぶ独立起業＆副業',
]

sns_list = [
    'https://qiita.com/13ryuji'
]
st.title('Maverick')
st.header('事業内容')
for i in biz_list:
    st.markdown('- ' + i)


st.header('実績')
for i in achievement_list:
    st.markdown('- ' + i)

st.header('SNS')
for i in sns_list:
    st.markdown('- ' + i)

st.header('ネタ')
for i in seed_list:
    st.markdown('- ' + i)

st.subheader('ボンズ　デモサイト')
for i in bonz_list:
    st.markdown('- ' + i)
