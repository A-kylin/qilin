
import codecs

import os

def character_2_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for lines in input_data.readlines():

        if lines == "\n":
            continue


        else:

            char_tag_pair = lines.strip().split('\t')

            char = char_tag_pair[0]
            tag = char_tag_pair[-1]


            if tag == "B-operationv":
                # if a!=0:
                output_data.write(char)

            elif tag == 'I-operationv':

                output_data.write(char)
            elif tag=='E-operationv':
                output_data.write(char+'\t'+tag+'\n')
            elif tag == 'B-part':

                output_data.write(char)

            elif tag == 'I-part':
                output_data.write(char)
            elif tag == 'E-part':
                output_data.write(char+'\t'+tag+'\n')
            elif tag == 'B-symptom':

                output_data.write(char)

            elif tag == 'I-symptom':
                output_data.write(char)
            elif tag == 'E-symptom':
                output_data.write(char +'\t'+tag+'\n' )
            elif tag == 'B-describe':

                output_data.write(char)

            elif tag == 'I-describe':
                output_data.write(char)
            elif tag == 'E-describe':
                output_data.write(char +'\t'+tag+'\n' )

            elif tag == 'B-medicine':

                output_data.write(char)

            elif tag == 'I-medicine':
                output_data.write(char)
            elif tag == 'E-medicine':
                output_data.write(char + '\t' + tag + '\n')

            elif tag == 'O':

                continue


    input_data.close()
    output_data.close()

def character_3_word(input_file, output_file):
    input_data = codecs.open(input_file, 'r', 'utf-8')
    output_data = codecs.open(output_file, 'w', 'utf-8')

    for lines in input_data.readlines():

        if lines == "\n":
            continue


        else:

            char_tag_pair = lines.strip().split('\t')

            char = char_tag_pair[0]
            tag = char_tag_pair[-1]



            if tag=='E-operationv':
                output_data.write('operationv'+'\t'+char+'\n')
            elif tag == 'E-part':
                output_data.write('part'+'\t'+char+'\n')

            elif tag == 'E-symptom':
                output_data.write('symptom'+'\t'+char +'\n')

            elif tag == 'E-describe':
                output_data.write('describe'+'\t'+char +'\n' )
            elif tag == 'E-medicine':
                output_data.write('medicine' + '\t' + char + '\n')




    input_data.close()
    output_data.close()
def name():
    input_file=os.getcwd() + "/end.txt"
    output_file = os.getcwd() + "/中间文本.txt"
    output_file1 = os.getcwd() + "/最后文本.txt"
    character_2_word(input_file, output_file)
    character_3_word(output_file, output_file1)
