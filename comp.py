import csv
import os
path='/home/ongraph/Desktop/CSV-2'
f=os.listdir(path)
n=False
X=[]
for x in sorted(f):
    s=path+"/"+x
    with open('/home/ongraph/Desktop/CSV-2/File00001.csv', 'r') as t1, open(s, 'r') as t2:
        fileone = t1.readlines()
        filetwo = t2.readlines()

        for line in filetwo:
            if line not in fileone:
                n=True
        if n==False:
            X.append(t2.name)
print(X)