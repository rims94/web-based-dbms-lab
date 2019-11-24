fhand=open('format.txt','r')
list=[]
for i in fhand:
    i=i.rstrip()
    i=i.rsplit()
    list.append(i)
print(list)