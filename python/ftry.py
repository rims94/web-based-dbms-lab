data = ['a,x', 'b,y', 'c,z']
f = open('leukemia_small.csv', 'wb')
w = csv.writer(f, delimiter = ',')
w.writerows([x.split(',') for x in data])
f.close()