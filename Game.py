#初始化
import random
import csv

#初始化函数
username = ''
randomnum = 0
inputnum = -1
time = 1




#开头
print('Hello')
username = input('Please set your user name:')
print('Hi ' +username+ ', here\'s a number between 0 and 100, let\'s Find out!')



#body
randomnum = random.randint(0,100)
print(randomnum)
while inputnum != randomnum :
    while True:
        inputnum = input('Let\'s Guess:')
        try:
            inputnum = int(inputnum)
        except ValueError:
            print('Please put a number here XD')
        else:
            break
    
    if inputnum < 0 or inputnum >100 :
        print('This number is between 1-100')
    else :
        if inputnum > randomnum :
            print('Try a smaller one')
            time = time + 1
        if inputnum < randomnum :
            print('Try a bigger one')
            time = time + 1
print('Congratulation' +username+'! You Find out the number in ' +str(time)+ ' times')  #finish

#写入排名
if username == '':
    username = 'unnamed'

result = [username,time]

csvfile = open('ranking.csv','a')
ranking = csv.writer(csvfile)
ranking.writerow(result)
csvfile.close()
#for i in ranking:
#print(ranking)


