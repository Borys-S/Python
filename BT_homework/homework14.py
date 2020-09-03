'''Task 1
Write a decorator that prints a function with arguments passed to it.
NOTE! It should print the function, not the result of its execution!
For example:
"add called with 4, 5"

def logger(func):
  pass
@logger
def add(x, y):
  return x + y
@logger
def square_all(*args):
  return [arg ** 2 for arg in args]'''

from functools import wraps

def logger(func):
  '''function which decorates other function'''
  print(f'Decorated function "{func.__name__}"')
  @wraps(func)
  def wrapper(*args, **kwargs):
    '''wrapper docstring will not be shown'''
    result = func(*args, **kwargs)
    print(f'Function {func.__name__} was called with parameters {args}.')
  return wrapper


@logger
def summing(a, b):
  '''This function summs 2 numbers "a" and "b"'''
  return a + b

summing(4, 5)
print(f'Function name is "{summing.__name__}".')
print(f'Function docstring is: {summing.__doc__}.')




'''Task 2
Write a decorator that takes a list of stop words and replaces them with * inside the decorated function
def stop_words(words: list):
    pass
@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan("Steve") == "Steve drinks * in his brand new *!"'''

# from functools import wraps
#
#
# def censorship(some_list=['pepsi', 'BMW']):
#   def inner_decorator(func):
#     print(f'Decorating function "{func.__name__}"...')
#     @wraps(func)
#     def wrap(*args, **kwargs):
#       decorated_str = func(*args, **kwargs)
#       for word in some_list:
#         decorated_str = decorated_str.replace(word, '*')
#       print(decorated_str)
#       return decorated_str
#     return wrap
#   return inner_decorator
#
#
# @censorship()
# def create_slogan(name):
#     return f'{name} drinks pepsi in his brand new BMW!'
#
# create_slogan('Mike')
#
#
# @censorship(some_list=['drinks', 'brand'])
# def another_slogan(name):
#     return f'{name} drinks pepsi in his brand new BMW!'
#
# another_slogan('Carl')




'''Task 3
Write a decorator `arg_rules` that validates arguments passed to the function.
A decorator should take 3 arguments:
max_length: 15
type_: str
contains: [] - list of symbols that an argument should contain
If some of the rules' checks returns False, the function should return False and print the reason it failed; otherwise, return the result.
def arg_rules(type_: type, max_length: int, contains: list):
@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"
assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'''

# from functools import wraps
#
# def arg_rules(type_, max_length, contains):
#   def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#       for arg in args:
#         if type(arg) is not type_:
#             print('Wrong type')
#             return False
#         if len(arg) > max_length:
#             print('Very long')
#             return False
#         for item in contains:
#             if item not in arg:
#                 print('Does\'nt contain some of required symbols')
#                 return False
#       print(func(*args, **kwargs))
#       return func(*args, **kwargs)
#     return wrapper
#   return decorator
#
#
# @arg_rules(type_=str, max_length=15, contains=['05', '@'])
# def create_slogan(name):
#     return f"{name} drinks pepsi in his brand new BMW!"
#
#
# create_slogan('fjkladsjgkjlkasdgjlkadsjkl')
# create_slogan('ldskj')
# create_slogan(1)
# create_slogan('pavel05@g.com')



