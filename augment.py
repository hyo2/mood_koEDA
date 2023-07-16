# Easy data augmentation techniques for text classification
# Jason Wei and Kai Zou

from eda import *

#arguments to be parsed from command line
import argparse

# 인자값을 받을 수 있는 인스턴스 생성
ap = argparse.ArgumentParser(description='emotion-joy data test 입니다.')

# 입력받을 인자값 등록(help: 인자가 하는 일에 대한 간단한 설명)
ap.add_argument("--input", required=True, type=str, help="input file of unaugmented data")
ap.add_argument("--output", required=False, type=str, help="output file of unaugmented data")
ap.add_argument("--num_aug", required=False, type=int, help="number of augmented sentences per original sentence")
ap.add_argument("--alpha_sr", required=False, type=float, help="percent of words in each sentence to be replaced by synonyms")
ap.add_argument("--alpha_ri", required=False, type=float, help="percent of words in each sentence to be inserted")
ap.add_argument("--alpha_rs", required=False, type=float, help="percent of words in each sentence to be swapped")
ap.add_argument("--alpha_rd", required=False, type=float, help="percent of words in each sentence to be deleted")

# 입력받은 인자값을 args에 저장 (type: namespace)
args = ap.parse_args()

#the output file
output = None
if args.output:
    output = args.output
else:
    from os.path import dirname, basename, join
    output = join(dirname(args.input), 'eda_' + basename(args.input))

#number of augmented sentences to generate per original sentence
num_aug = 1 #default=9
if args.num_aug:
    num_aug = args.num_aug

#how much to replace each word by synonyms
#각 단어를 동의어로 대체하는 정도
alpha_sr = 0.2 #default=0.1
if args.alpha_sr is not None:
    alpha_sr = args.alpha_sr

#how much to insert new words that are synonyms
#동의어인 새 단어를 삽입하는 정도
alpha_ri = 0 #default=0.1
if args.alpha_ri is not None:
    alpha_ri = args.alpha_ri

#how much to swap words
#얼마나 많은 단어를 교환
alpha_rs = 0.3 #default=0.1
if args.alpha_rs is not None:
    alpha_rs = args.alpha_rs

#how much to delete words
#단어를 삭제하는 정도
alpha_rd = 0.1 #default=0.1
if args.alpha_rd is not None:
    alpha_rd = args.alpha_rd

if alpha_sr == alpha_ri == alpha_rs == alpha_rd == 0:
     ap.error('At least one alpha should be greater than zero')

#generate more data with standard augmentation
def gen_eda(train_orig, output_file, alpha_sr, alpha_ri, alpha_rs, alpha_rd, num_aug=9):

    writer = open(output_file, 'w',encoding='UTF-8')
    lines = open(train_orig, "rt", encoding='UTF-8').readlines()

    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')
        label = parts[0]
        sentence = parts[1]
        aug_sentences = EDA(sentence, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, p_rd=alpha_rd, num_aug=num_aug)
        for aug_sentence in aug_sentences:
            writer.write(label + "\t" + aug_sentence + '\n')

    writer.close()
    print("generated augmented sentences with eda for " + train_orig + " to " + output_file + " with num_aug=" + str(num_aug))

#main function
if __name__ == "__main__":

    #generate augmented sentences and output into a new file
    gen_eda(args.input, output, alpha_sr=alpha_sr, alpha_ri=alpha_ri, alpha_rs=alpha_rs, alpha_rd=alpha_rd, num_aug=num_aug)