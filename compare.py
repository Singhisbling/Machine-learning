import csv
import os
"""path='/home/ongraph/Desktop/Untitled Folder'
f=os.listdir(path)
for x in sorted(f):
    s=path+"/"+x
    y=open(s,'r')
    read=csv.reader(y)
    read.__next__()
    for i in read:"""




with open('/home/ongraph/Desktop/CSV-2/File00001.csv', 'r') as t1, open('/home/ongraph/Desktop/CSV-2/File00004.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('update.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
