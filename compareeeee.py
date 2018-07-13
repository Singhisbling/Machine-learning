import csv
import os
path='/home/ongraph/Desktop/CSV-2'
f=os.listdir(path)
n=False
X=[]
s=0
p=0
with open('/home/ongraph/Desktop/CSV-2/File00002.csv', 'r') as t1:
    with open('/home/ongraph/Desktop/CSV-2/File00002.csv', 'r') as t2:
        same = set(t1).intersection(t2)
        if len(same)==217361:
            X.append(t2.name)

    #for line in sorted(same):
    #print(line)
print(X)