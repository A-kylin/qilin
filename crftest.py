import os
import codecs
def CRFTEST():

    os.system('crf_test -m model test >> result.txt')
    print('训练成功')
def CRFTEST1():
    input_file=os.getcwd()+"/end.txt"
    input_data= codecs.open(input_file, "w", 'utf-8')
    input_data.write("")
    input_data.close()
    os.system('crf_test -m model input.txt >> end.txt')
