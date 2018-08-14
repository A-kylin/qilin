
import codecs

import os


def prf1():
    input_file=os.getcwd() + "/result.txt"
    input_data = codecs.open(input_file, 'r', 'utf-8')
    ture = 0
    a = 0
    b = 0

    for lines in input_data.readlines():

        if lines == "\n":
            continue

        else:

            char_tag_pair = lines.strip().split('\t')

            char = char_tag_pair[0]
            tag= char_tag_pair[-2]
            tag1=char_tag_pair[-1]

            if tag != "O" and tag==tag1:
                 ture=ture+1
            elif tag == "O" and tag1!="O":
                    a=a+1
            elif tag!="O" and tag1=="O":
                b=b+1

    input_data.close()
    P=ture/(ture+a)
    R=ture/(ture+b)
    F=(2*P*R)/(P+R)
    print("P准确率：\t",end=' ')
    print(P)
    print("R召回率：\t",end=' ')
    print(R)
    print("F值：\t",end=' ')
    print(F)
