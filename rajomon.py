import re
import streamlit as st
import numpy as np
import random

#テキストの読み込み
source = '羅城門単語.txt'

f = open(source, encoding='utf-8')
d = f.read()
f.close()
#print(d)

#答えの読み込み
source2 = '羅城門単語答え.txt'
f2 = open(source2, encoding='utf-8')
d2 = f2.read()
f2.close()
#print(d2)

#データのリスト化（正規表現）
values = re.findall(r'[^a-z\n]+', d)
#print(values)

keys = re.findall(r'[^a-z\n]+', d2)
#print(keys)

word_dict = dict(zip(values, keys))
#print(word_dict)

#Streamlitコード

st.title('羅城門単語確認')

"""

### 次の( )の単語を現代語に直しなさい

"""

question_w = random.choice(values)
#print(question_w)
correct_a = word_dict[question_w]
#print(correct_a)


st.header(question_w)

expander = st.beta_expander('答えを表示する')
expander.header(correct_a)

button = st.button('次の問題を表示する')





