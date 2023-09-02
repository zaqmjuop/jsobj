# - bool 不可变数据类型，有2个值：True和False
True = False # 重新赋值会报错
"""
  Cell In[49], line 1
    True = False
    ^
SyntaxError: cannot assign to True
"""
del True # 无法被删除
"""
  Cell In[50], line 1
    del True
        ^
SyntaxError: cannot delete True
"""
### 类型转换
bool('') # False
bool(' ') # True
bool('hello') # True
bool(None) # False

# - None 不可变数据类型，有1个值：None
print(None) # None
print(type(None)) # <class 'NoneType'>
print(isinstance(None, type(None))) # True
None == None # True
None is None # True

# - int和float,不可变数据类型
type(1) # int
type(1.0) # float
isinstance(1, int) # True
isinstance(1, float) # False
isinstance(1.0, int) # False
isinstance(1.0, float) # True
print(0xA0F) # 2575 # 16进制数字
print(0o37) # 31 # 8进制数字
### 类型转换
int(1.0) # 1
int('1') # 1
int('') # ValueError: invalid literal for int() with base 10: ''
int('1.1') # ValueError: invalid literal for int() with base 10: '1.1'
int('hello') # ValueError: invalid literal for int() with base 10: 'hello'
int(None) # TypeError: int() argument must be a string, a bytes-like object or a number, not 'NoneType'
int(True) # 1
int(False) # 0
float(1) # 1.0
float('') # ValueError: could not convert string to float: ''
float('1') # 1.0
float('1.1') # 1.1
float('hello') # ValueError: could not convert string to float: 'hello'
float(True) # 1.0
float(False) # 0.0
hex(256) # '0x100' # 转16进制
bin(255) # '0b11111111' # 转2进制
### 比较大小
print(0 < 1) # True
print(0 <= 0) # True
print(0 > 0) # False
print(0 >= 0) # True
# 计算和赋值
num1 = 0
print(num1 + 1) # 1
num1 += 1
print(num1) # 1

# - str 不可变数据
str1 = 'hello world'
str2 = """
def strConcat(str1, str2):
    return str1 + str2
""" # '\ndef strConcat(str1, str2):\n    return str1 + str2\n' # 多行字符串
str3 = f"hello {'world'}" # 'hello world' # 字符串插值
len(str3) # 51 # 返回目标长度
print('hel' + 'lo') # 'hello' # 组合
