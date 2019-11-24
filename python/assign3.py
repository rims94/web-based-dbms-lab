fhand=open('format.txt','r')
list=[]
for i in fhand:
    i=i.rstrip()
    list.append([i])
print(list)