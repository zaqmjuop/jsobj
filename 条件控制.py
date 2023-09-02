# if: elif: else: 对应if() {}else if(){}else{}
if(False):
  print('if')
elif(False): # 可选
  print('else if')
else: # 可选
  print('else')

# == 、!= 、is 对应 ==、!=、===
### - == 是判断值相等的符号
print('hello' == 'hello') # True
print('hello' == 'hello world') # False
### - != 是判断值不等的符号
print('hello' != 'hello') # False
print('hello' != 'hello world') # True
### - is 是判断内存地址是否相同的符号
print('hello' is 'hello') """SyntaxWarning: "is" with a literal. Did you mean "=="? print('hello' is 'hello')"""
print(print is print) # True
# and、or、not、not is  对应&&、||、!、!==
print(True and True) # True
print(False and False) # False
print(False and True) # False
print(True and False) # False
print('' and 'hello') # ''
print('hello' and '') # ''
print('hello' and 'hello') # 'hello' 

print(True or True) # True 
print(False or False) # False
print(False or True) # True
print(True or False) # True
print('' or '') # ''
print('' or 'hello') # 'hello'
print('hello' or '') # 'hello'
print('hello' or 'hello') # 'hello' 

print(not True) # False
print(not False) # True
print(not '') # True
print(not 'hello') # False
print(not (True and True)) # False
# 三元表达式  'true res' if True else 'false res' 对应 true ? 'true res' : 'false res'
print('true res' if True else 'false res' ) # true res
print('true res' if False else 'false res' ) # false res
# match 对应 switch  ##python3.10之后才有
my_str = 'hello world'
match my_str:
  case 'hello':
    return my_str
  case 'hello world':
    return my_str
  case _: # 无视条件直接捕获
    return my_str
# type 对应 typeof 
type('hello') # str
type(type('hello')) # type
type(type(type('hello'))) # type
# isinstance 对应 instanceof
isinstance('hello', type('hello')) # True
isinstance('hello', type(type('hello'))) # False
isinstance(str, type(type('hello'))) # True
isinstance(type, type(type('hello'))) # True
