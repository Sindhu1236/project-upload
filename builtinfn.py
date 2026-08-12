# math
'''import math
n=int(input("enter the number"))
print("square root",math.sqrt(n))
print("factorial",math.factorial(n))
base=int(input("enter base"))
power=int(input("enter power"))
print("power",math.pow(base,power))
'''
# random
'''import random
print("random int",random.randint(1,2))
''''''print(f"random number from range,{random.randrange(10,50)}random float{random.random()} random decimal{random.uniform(1,10)}")
f=["apple","mango"]
print(f" random fruit{random.choice(f)} random 3 fruits{random.choice(f,k=1)}")'''
'''n=[10,20,30,40]
random.shuffle(n)'''
# datetime
'''from datetime import datetime,date,timedelta
now=datetime.now()#current date,time
print(now)
today=date.today()# todays date
print(today)

print(f'year,{now.year}month{now.month} day{now.day}')
print(f'hour{now.hour} minute{now.minute} second{now.second}')
print(f" formatted date{now.strftime("%D-%m-%y")} formatted time{now.strftime("%h-%m-%S")} ")
'''
# time
import time
'''print(f" current time in seconds:{time.time()} current time readable time:{time.ctime()} ")
print('foematted date:',time.strftime("%D-%m-%y"))
print('foematted date:',time.strftime("%H-%M_%S"))'''
start=time.perf_counter()
for i in range(1000000):
    pass
end=time.perf_counter()
print("execution time",end-start,"seconds")

