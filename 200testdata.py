import os

n=401
while n<=600:

    finalname=os.getcwd()+"/alldata/"+str(n)
    finalname1 = os.getcwd() +"/test"
    f1=open(finalname,"r")
    f2 = open(finalname1, "a")
    for line1 in f1.readlines():
        f2.write(line1)
    n=n+1
    f1.close()
print("200个测试文件")