import os


n=3
while n<=400:

    finalname=os.getcwd()+"/alldata/"+str(n)
    finalname1 = os.getcwd() + "/train"
    f1=open(finalname,"r")
    f2 = open(finalname1, "a")
    for line1 in f1.readlines():
        f2.write(line1)
    f1.close()
    n=n+1
print("400个训练文件")
