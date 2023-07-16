set_eda_joy = open('data/set_eda/set_eda_joy','w',encoding='UTF-8')
eda_joy = open('data/emotion/labeled/eda_labeled_joy', 'r',encoding='UTF-8')

joy_lines = eda_joy.readlines()

# deduplication
set_joy_lines = list(set(joy_lines))

# unlabeling
def unlabeling(line):
    parts = line[:-1].split('\t')
    label = parts[0]
    sentence = parts[1]
    return sentence

# unlabeling joy
for line in set_joy_lines:
    sentence = unlabeling(line)
    set_eda_joy.write(sentence + '\n')

# close files
set_eda_joy.close()
eda_joy.close()