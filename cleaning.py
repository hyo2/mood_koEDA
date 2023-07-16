import re
from hanspell import spell_checker
from soynlp.normalizer import *

cleaned_angry = open('data/cleaned_data/cleaned_angry','w',encoding='UTF-8')
unlabeled_angry = open('data/emotion/unlabeled/unlabeled_angry','r',encoding='UTF-8')

cleaned_sad = open('data/cleaned_data/cleaned_sad','w',encoding='UTF-8')
unlabeled_sad = open('data/emotion/unlabeled/unlabeled_sad','r',encoding='UTF-8')

cleaned_soso = open('data/cleaned_data/cleaned_soso','w',encoding='UTF-8')
unlabeled_soso = open('data/emotion/unlabeled/unlabeled_soso','r',encoding='UTF-8')

cleaned_happy = open('data/cleaned_data/cleaned_happy','w',encoding='UTF-8')
unlabeled_happy = open('data/emotion/unlabeled/unlabeled_happy','r',encoding='UTF-8')

cleaned_joy = open('data/cleaned_data/cleaned_joy','w',encoding='UTF-8')
unlabeled2_joy = open('data/emotion/unlabeled/unlabeled2_joy', 'r',encoding='UTF-8')

def cleaning(line):
    parseText = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+').sub('', line)

    spelled_sent = spell_checker.check(parseText)
    checkedText = spelled_sent.checked # 맞춤법 교정 후 문장 저장(띄어쓰기까지 교정함)

    refinedText = repeat_normalize(checkedText, num_repeats=2) # 반복 문자 정제(ex) ㅋㅋㅋㅋㅋ, ㅎㅎㅎ)
    return refinedText

angry_lines = unlabeled_angry.readlines()
sad_lines = unlabeled_sad.readlines()
soso_lines = unlabeled_soso.readlines()
happy_lines = unlabeled_happy.readlines()
joy_lines = unlabeled2_joy.readlines()

# cleaning emotions
for line in angry_lines:
    line = cleaning(line)
    cleaned_angry.write(line + '\n')

for line in sad_lines:
    line = cleaning(line)
    cleaned_sad.write(line + '\n')

for line in soso_lines:
    line = cleaning(line)
    cleaned_soso.write(line + '\n')

for line in happy_lines:
    line = cleaning(line)
    cleaned_happy.write(line + '\n')

for line in joy_lines:
    line = cleaning(line)
    cleaned_joy.write(line + '\n')

# close files
cleaned_angry.close()
unlabeled_angry.close()

cleaned_sad.close()
unlabeled_sad.close()

cleaned_soso.close()
unlabeled_soso.close()

cleaned_happy.close()
unlabeled_happy.close()

cleaned_joy.close()
unlabeled2_joy.close()