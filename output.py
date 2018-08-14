import os

def output1():
    finalname=os.getcwd()+"/最后文本.txt"
    finalname1=os.getcwd()+"/最后文本2.txt"
    f1=open(finalname,"r")

    line1=f1.read()
    f1.close()
    line=line1.split('\n')
    a=0
    b=1
    c=len(line)
    line4=[]
    line5=[]
    while b<c:
            line2=line[a].split('\t')
            line3=line[b].split('\t')
            if line2[0]=="part" and line3[0]=='describe':
                line4.append(line3[0])
                line4.append(line2[1]+line3[1])
                line5.append(a)
            a=a+1
            b=b+1
    line4=list(set(line4))

    d=len(line5)
    e=0
    while e<d:
        del line[int(line5[e])-e*2]
        del line[int(line5[e])-e*2]
        e=e+1

    line=list(set(line))
    f2 = open(finalname1, "w")
    c = len(line)
    a = 0

    f2.write("解剖部位：")
    print("解剖部位：", end=" ")
    while a < c:
        line6 = line[a].split('\t')
        if line6[0] == "part":
            f2.write(line6[1]+".")
            print(line6[1], end=" ")
        a = a + 1
    print("")
    f2.write('\n')

    f2.write("症状描述：")
    f=len(line4)
    g=0
    print("症状描述：",end=" ")
    while g<f:

        if line4[g]!="describe":
            f2.write(line4[g]+".")
            print(line4[g],end=" ")
        g=g+1

    c = len(line)
    a = 0
    while a < c:
        line6 = line[a].split('\t')
        if line6[0] == "describe":
            f2.write(line6[1] + ".")
            print(line6[1], end=" ")
        a = a + 1
    print("")
    f2.write('\n')

    f2.write("独立症状：")
    c = len(line)
    a = 0
    print("独立症状：", end=" ")
    while a < c:
        line6 = line[a].split('\t')
        if line6[0] == "symptom":
            f2.write(line6[1] + ".")
            print(line6[1], end=" ")
        a = a + 1
    print("")
    f2.write('\n')

    f2.write("手术：")
    c = len(line)
    a = 0
    print("手术：", end=" ")
    while a < c:
        line6 = line[a].split('\t')
        if line6[0] == "operationv":
            f2.write(line6[1] + ".")
            print(line6[1], end=" ")
        a = a + 1
    print("")
    f2.write('\n')

    f2.write("药物：")
    c = len(line)
    a = 0
    print("药物：", end=" ")
    while a < c:
        line6 = line[a].split('\t')
        if line6[0] == "medicine":
            f2.write(line6[1] + ".")
            print(line6[1], end=" ")
        a = a + 1
    print("")
    f2.write('\n')

    f2.close()

