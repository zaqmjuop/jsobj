# JavaScript 对象参考手册 https://www.w3school.com.cn/jsref/jsref_obj_object.asp
#  a === b: boolean  Object.is(a, b)
def objectis(a,b):
    return a is b

print(objectis({}, {})) # False

# Object.keys(record: Record<string, string>): string[]
def objKeys(record):
    return list(record.keys())


print(objKeys(my_dict), type(my_dict)) # ['key1', 'key2', 'key3', 'key4'] <class 'dict'>

# 判断字典中是否存在键
print('key1' in my_dict) # True
print('key-1' in my_dict) # False
# 增加值或修改值
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
my_dict['key4'] = '44'
my_dict # {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': '44'}

# 删除值
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
del my_dict['key2']
my_dict # {'key1': 'value1', 'key3': 'value3'}

# Object.assign(obj1: Record<string, string>, obj2: Record<string, string>): Record<string, string>
def objectAssign(obj1, obj2):
    obj1.update(obj2)
    return obj1

print(objectAssign({'Name': 'W3CSchool', 'Age': 7}, {'Sex': 'female', 'Age': 8})) # {'Name': 'W3CSchool', 'Age': 8, 'Sex': 'female'}
