import os
import codecs

def input1():
    input_file=os.getcwd() + "/input.txt"
    input_string = input('请输入:')
    input_data = codecs.open(input_file, 'w', 'utf-8')
    for m in input_string:
        input_data.write(m+'\n')
    input_data.close()
def input2(data):
    input_file = os.getcwd() + "/input.txt"
    input_string =data
    input_data = codecs.open(input_file, 'w', 'utf-8')
    for m in input_string:
        input_data.write(m + '\n')
    input_data.close()