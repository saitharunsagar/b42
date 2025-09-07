Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
b=20
a,b = b,a
print(a)
20
print(b)
10
id(a)
140728300555288
id(b)
140728300554968
del a
print(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined
del b
print(b)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined
a= input()
print(a)
10
10
a = input('enter a number')
enter a number10
print(a)
10
a = input('enter a number')
enter a number10
a = input('Enter a number : ')
Enter a number : 10
a = input('Enter a number : \n') print(a)
SyntaxError: invalid syntax
a = input('Enter a number : \n')
Enter a number : 
10
 print(a)
 
SyntaxError: unexpected indent
a = input('Enter a number : {a}\n')
Enter a number : {a}
a = input(f'Enter a number : {a}\n')
10
10
a = input('enter a number : ')
enter a number : 10
print(a)
10
a = none
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a = none
NameError: name 'none' is not defined. Did you mean: 'None'?
a = None
print(a)
None
type(a)
<class 'NoneType'>
calc()
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    calc()
NameError: name 'calc' is not defined
a = 10
if(a==None):
    print('does not return any values')

elif(a=10):
    
SyntaxError: invalid syntax
elif(a==10);
SyntaxError: invalid syntax
elif(a==10):
    
SyntaxError: invalid syntax
a = 10
if(a==None):
    print('does not return any values')
    
SyntaxError: multiple statements found while compiling a single statement
a = 10
if(a==None):
    print('does noa = 10
          
SyntaxError: unterminated string literal (detected at line 2)
a = 10
          
b = None
          
if(a==b)
          
SyntaxError: expected ':'
a=10
          
b =20
          
if(a==b):
          print(f'{a} is equal to {b}')
elif(a!=b):
    print(f'{a} is not qual to {b}')
else:
    print('Either postive nor negative')

10 is not qual to 20

================================================================= RESTART: C:/Users/Ajay/Desktop/python/current_bill.py ================================================================
enter current reading500
enter previous reading1000
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/current_bill.py", line 3, in <module>
    units = previous_reading - current_reading
TypeError: unsupported operand type(s) for -: 'str' and 'str'

================================================================= RESTART: C:/Users/Ajay/Desktop/python/current_bill.py ================================================================
enter current reading: 500
enter previous reading: 1000
Enter a Gender: M
enter unit rate10
The unit rate for Male :  5000

================================================================= RESTART: C:/Users/Ajay/Desktop/python/current_bill.py ================================================================
enter current reading: 500
enter previous reading: 1000
Enter a Gender:   M
The unit rate for Male :  5000

================================================================= RESTART: C:/Users/Ajay/Desktop/python/current_bill.py ================================================================
enter current reading: 400
enter previous reading: 600
Enter a Gender:   F
The unit rate for Female :  400

================================================================= RESTART: C:/Users/Ajay/Desktop/python/current_bill.py ================================================================
enter current reading: 300
enter previous reading: 100
Enter a Gender:   M
The unit rate for Male :  800
The unit rate for Male :  800
SyntaxError: invalid syntax


================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 15, in <module>
    b = byte(a)
NameError: name 'byte' is not defined. Did you mean: 'bytes'?

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 21, in <module>
    b = bytes(a)
ValueError: bytes must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 21, in <module>
    b = bytes(a)
ValueError: bytes must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 21, in <module>
    b = bytes(a)
ValueError: bytes must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
b'\x01\x1e\xc8\x14\x1e'
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 41, in <module>
    b = bytearray(a)
ValueError: byte must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
b'\x01\x1e\xc8\x14\x1e'
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 41, in <module>
    c= bytearray(a)
ValueError: byte must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
b'\x01\x1e\xc8\x14\x1e'
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 41, in <module>
    c = bytearray(a)
ValueError: byte must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
b'\x01\x14\x1e(2('
1
b'\x01\x1e\xc8\x14\x1e'
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 41, in <module>
    c = bytearray(a)
ValueError: byte must be in range(0, 256)

================================================================== RESTART: C:/Users/Ajay/Desktop/python/datatypes.py ==================================================================
vaarahi
v
ara
arahi
vaarahivaarahi
vaarahiINSTITUTE
Traceback (most recent call last):
  File "C:/Users/Ajay/Desktop/python/datatypes.py", line 43, in <module>
    c = bytearray(a)
ValueError: byte must be in range(0, 256)
ValueError: byte must be in range(0, 256)
          
SyntaxError: invalid syntax
a = [101,'ravi','NRT']
          
b = [102,'Raju','HYD']
          
a[0]
          
101
print(a)
          
[101, 'ravi', 'NRT']
type(a)
          
<class 'list'>
a[4] = 'saitharun'
          
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    a[4] = 'saitharun'
IndexError: list assignment index out of range
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
          
print(list)
          
['abcd', 786, 2.23, 'john', 70.2]
help('keywords')
          

Here is a list of the Python keywords.  Enter any keyword to get more help.

False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not                 

list[0]
'abcd'
>>> print(list[2:3])
[2.23]
>>> print(list[3:])
['john', 70.2]
>>> print(list*2)
['abcd', 786, 2.23, 'john', 70.2, 'abcd', 786, 2.23, 'john', 70.2]
>>> tinylist = [123, 'john']
>>> list+tinylist
['abcd', 786, 2.23, 'john', 70.2, 123, 'john']
>>> a = (1,2,3,4,5,6,7,7,3,2,1)
>>> print(a)
(1, 2, 3, 4, 5, 6, 7, 7, 3, 2, 1)
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> dir(a)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']
>>> type(a)
<class 'tuple'>
>>> list[0] = 'apple'
>>> print(list)
['apple', 786, 2.23, 'john', 70.2]
>>> a[0] = 'sagar'
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    a[0] = 'sagar'
TypeError: 'tuple' object does not support item assignment
>>> a = range(10)
>>> print(a)
range(0, 10)
>>> for i in a:
...     print(i)
... 
0
1
2
3
4
5
6
7
8
9
