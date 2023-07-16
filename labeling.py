labeled2_joy = open('data/emotion/labeled/labeled2_joy','w',encoding='UTF-8')
unlabeled2_joy = open('data/emotion/unlabeled/unlabeled2_joy', 'r',encoding='UTF-8')

joy_lines = unlabeled2_joy.readlines()

# labeling emotions

for line in joy_lines:
    labeled2_joy.write('4' + '\t' + line)

# close files
labeled2_joy.close()
unlabeled2_joy.close()