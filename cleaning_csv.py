import re
from hanspell import spell_checker
from soynlp.normalizer import *

import pandas as pd

import os

emotion_add = pd.read_csv('C:/Users/Hi/Downloads/emotion_add_joy.csv')

def cleaning(line):
    parseText = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+').sub('', line)

    spelled_sent = spell_checker.check(parseText)
    checkedText = spelled_sent.checked # 맞춤법 교정 후 문장 저장(띄어쓰기까지 교정함)

    refinedText = repeat_normalize(checkedText, num_repeats=2) # 반복 문자 정제(ex) ㅋㅋㅋㅋㅋ, ㅎㅎㅎ)
    return refinedText

emotion_add['Sentence'] = emotion_add['Sentence'].apply(cleaning)
# print(emotion_add)

f_path = 'C:/Users/Hi/Desktop/'
f_name = "emotions_clean.csv"

emotion_add.to_csv(os.path.join(f_path, f_name), index=False)