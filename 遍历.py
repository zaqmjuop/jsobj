# while
i = 0
str1 = 'hello world'
while(i < len(str1)):
    print(str1[i])
    i += 1
# h , h
# e , he
# l , hel
# l , hell
# o , hello
#   , hello 
# w , hello w
# o , hello wo
# r , hello wor
# l , hello worl
# d , hello world

# for
for char in 'hello world':
    print(char)
# h
# e
# l
# l
# o
#  
# w
# o
# r
# l
# d

# range对象
for i in range(0, 5, 1): # 相当于 for(var i = 0, i < 5; i++){ console.log(i) }
    print(i)
# 0
# 1
# 2
# 3
# 4

# - range(start: int, stop: int, step: int): range
r = range(0, 5, 1) # range(0, 5)
len(r) # 5
r[0] # 0
r[1] # 1
r[5] # IndexError: range object index out of range
# - 修改开始和结束范围
for i in range(3, 10, 1): # 相当于 for(var i = 3, i < 10; i += 1){ console.log(i) }
    print(i)
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# - 修改步进
for i in range(1, 10, 2): # 相当于 for(var i = 3, i < 10; i += 2){ console.log(i) }
    print(i)
# 1
# 3
# 5
# 7
# 9
# - 从大到小
for i in range(10, 2, -2): # 相当于 for(var i = 10, i > 2; i -= 2){ console.log(i) }
    print(i)
# 10
# 8
# 6
# 4

# continue break pass
for i in range(0, 5, 1):  # 相当于 for(var i = 0, i < 5; i++){ ... }
    if(i == 1):
        print(i, 'continue')
        continue
    if(i == 2):
        print(i, 'pass')
        pass
    if(i == 3):
        print(i, 'break')
        break
    print(i)
# 0
# 1 continue
# 2 pass
# 2
# 3 break

# 主线程阻塞
"""
js中阻塞主线程的方式
stopT = new Date(new Date().getTime() + 999)
while(new Date().getTime() < stopT.getTime()) { console.log(1) } # 打印若干个 1
"""
# - 同样的逻辑在python里的写法
import datetime # 相当于js中的Date

count = 0
stopT = datetime.datetime.now() + datetime.timedelta(seconds=0.99)

while datetime.datetime.now() < stopT:
    count += 1

print("计数结束，共计数", count, "次") # 计数结束，共计数 1561638 次
# - python里内置的阻塞主线程的方法
import time

print("开始")
time.sleep(0.99)
print('结束')
# 开始
# 结束

# - while(true){} 在python里的写法
while True:
  pass
