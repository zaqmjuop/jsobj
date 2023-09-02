# js中的异常处理 try catch finally throw Error
"""
try {
  throw new Error('自定义异常')
} catch(err) {
  console.error(err)
} finally {
  console.log('finally')
}
"""
try:
  raise Exception('自定义异常')
except Exception as e:
  print(e, type(e), e.args[0]) # 自定义异常 <class 'Exception'> 自定义异常
finally:
  print('finally') # finally
