import csv
import os
path='/home/ongraph/Desktop/CSV-2'
f=os.listdir(path)
n=False
X=[]
for x in sorted(f):
    for x in sorted(f):
        s=path+"/"+x
        with open(s, 'r') as t1, open(s, 'r') as t2:
            same = set(t1).intersection(t2)
            if len(same)==217361:
                X.append(t2.name)


print(X)