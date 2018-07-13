import csv
from matplotlib import pyplot as plt
import os
from colormap import rgb2hex
path='/home/ongraph/Desktop/CSV-2'
f=os.listdir(path)
X=[]
Y=[]
c=[]
m=[]
for h in range(1,217362):
    for x in sorted(f):
        s = path + "/" + x
        y = open(s, 'r')
        read = csv.reader(y)
        for q in range(0,h):
            read.__next__()

        for i in read:
            X.append(i[0])
            Y.append(i[1])
            c.append(rgb2hex(int(i[2]), int(i[3]), int(i[4])))
            break
            if c[1:] == c[:-1]:
                m.append([i[0],i[1],c[0]])


with open("/home/ongraph/Desktop/fssst.csv", 'w') as g:
    csvRow = csv.writer(g, dialect='excel')
    csvRow.writerow(m)

