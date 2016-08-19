# -*- coding: utf-8 -*-
# print('hello, world')
# name = input()
# print('hello,', name)

from functools import reduce

def str2int(s):
	def fn(x, y):
		return x*10+y
	def char2num(s):
		return {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}[s]
	return reduce(fn, map(char2num, s))

print(str2int('13579'))

# 用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 接受一个list并利用reduce()求积
def prod(L):
    return reduce(lambda x,y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


def str2float(s):
    return reduce(lambda x, y : x + y/(10**len(str(y))), map(int, s.split('.')))


def _odd_iter():
	n = 1
	while True:
		n = n+2
		yield n
def not_divisible(n):
	return lambda x: x%n > 0
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(not_divisible(n), it)


def is_palindrome(n):
    n=str(n)
    return n[::]==n[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

# splice
# 删除 ----  item不设置
# 替换 ---- item为替换的值
# 添加 ----  len设置为0，item为添加的值

import functools

def log(*args_out):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			if (callable(args_out[0])):
				print('begin %s()' % (func.__name__))
			else:
				print('begin %s %s()' % (args_out[0], func.__name__))
			
			# return func(*args, **kw)
			r = func(*args, **kw)
			print('end call')
			return r
		return wrapper
	if (callable(args_out[0])):
		return decorator(args_out[0])
	else: return decorator

@log('call')
def now():
	print('2016-7-21')
now()

int2 = functools.partial(int, base=2)
print(int2('10010'))
print(int2('10010', base=10))


' a test module '
__author__ = 'Michael Liao'
import sys
def test():
    args = sys.argv
    if len(args)==1:
            print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')
if __name__=='__main__':
    test()
#直接在cmd运行hello.py文件，__name__的值就是__main__，所以就直接调用test()函数，输出hello world
#如果是先启动python环境，再import hello模块，__name__的值就是模块名hello，所以要在cmd输入hello.test()才能调用test函数


def print_score(std):
	print('%s %s' % (std['name'], std['score']))

std1 = { 'name': 'Michael', 'score': 98 }
std2 = { 'name': 'Bob', 'score': 81 }

print_score(std1)
print_score(std2)


class Student(object):
	def __init__(self, name, score):
		self.name = name
		self.score = score
	def print_score(self):
		print('%s: %s' % (self.name, self.score))

cht = Student('Haitao chen', 86)
ctz = Student('Tongzhao cai', 92)
hjw = Student('Jianwu huang', 90)
cht.print_score()
ctz.print_score()
hjw.print_score()


class Animal(object):
	def run(self):
		print('Animal is running.')

class Dog(object):
	def run(self):
		print('Dog is running.')

class Cat(object):
	def run(self):
		print('Cat is running.')

animal = Animal()
dog = Dog()
cat = Cat()

animal.run()
dog.run()
cat.run()

class stu(object):
	name = 'Student'

a=stu()
print('a.name: ', a.name)
print('stu().name: ', stu().name)
a.name='cht'
print('a.name: ', a.name)
print('stu().name: ', stu().name)
del a.name
print('a.name: ', a.name)
print('stu().name: ', stu().name)


class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer!')
        if value <= 0:
            raise ValueError('width must be greater than 0')
        self._width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise ValueError('height must be an integer!')
        if value <= 0:
            raise ValueError('height must be greater than 0')
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height

# test:
s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution

from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
	print(name, '=>', member, ',', member.value)

from enum import Enum, unique
@unique
class Weekday(Enum):
	Sun = 0
	Mon = 1
	Tue = 2
	Wed = 3
	Thu = 4
	Fri = 5
	Sat = 6

print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(Weekday(1))
day1 = Weekday.Mon
print(day1)


class Hello(object):
	def hello(self, name='world'):
		print('hello, %s' % name)

from hello import Hello
h=Hello()
h.hello()
print(type(Hello))
print(type(h))

import logging

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)

main()
print('END')

def f():
	try:
	    print('try...')
	    r = 10 / int('2')
	    print('result:', r)
	except ValueError as e:
	    print('ValueError:', e)
	except ZeroDivisionError as e:
	    print('ZeroDivisionError:', e)
	else:
	    print('no error!')
	finally:
	    print('finally...')
	print('END')

f()

# import pdb
# s = '0'
# n = int(s)
# pdb.set_trace()
# print(10 / n)


from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d)
