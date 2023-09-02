# 声明一个列表
list1 = [
  "你的爱好是r什么？",
  "我的爱好是，踢 足 球"
] # ['你的爱好是r什么？', '我的爱好是，踢 足 球']
# 查看列表的属性
print(type(list1)) # <class 'list'>
isinstance(list1, list) # True
len(list1) # 2
list1[0] # '你的爱好是r什么？'
list1[1] # '我的爱好是，踢 足 球'
list1[2] # IndexError: list index out of range
# - 遍历
"""
for(var line of list1){ console.log(line) }
"""
for line in list1:
    print(line)
# - 当赋值索引-1时，js和python有区别
"""
list1[-1] = '你妈妈，击碎！'
list1.length // 2
list1 // ['你的爱好是r什么？', '我的爱好是，踢 足 球', -1: '你妈妈，几岁！']
"""
list1[-1] = '你妈妈，几岁！'
len(list1) # 2
list1 # ['你的爱好是r什么？', '你妈妈，几岁！']

# 声明一个字典
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} // {key1: 'value1', key2: 'value2', key3: 'value3'}
"""
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'} # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# 查看字典的属性
len(my_dict) # 3
type(my_dict) # dict
isinstance(my_dict , dict) # True
my_dict['key1'] # 'value1'
my_dict['key1'] = 'change value 1'
my_dict['key1'] # 'change value 1'
my_dict.key1 # AttributeError: 'dict' object has no attribute 'key1'
# - 遍历
"""
for(key in my_dict){ console.log(key) } // key1 key2 key3
"""
for key in my_dict:
    print(key)
# key1 key2 key3
