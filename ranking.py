import csv
list = []
csvfile = open('ranking.csv','r')
ranking = csv.reader(csvfile)

t = 0
for i in ranking:
    t = t + 1
    if (t % 2) == 0:
        pass
    else:
        list.append(i)
#print(list)

for j in list:
    ilist = j
    print('username:' +ilist[0]+ ' ,times' +ilist[1])