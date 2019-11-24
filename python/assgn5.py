import csv
fhand=open('data.csv','r')
inp=csv.reader(fhand)
list=[]
for row in inp:
    list.append(row)
print(list)