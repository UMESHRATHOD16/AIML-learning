# File handling anf behind the sences of loops
f = open('chai.py')
f.readline()
'import time\n'
f.readline()
'print("Chai is here")\n'
f.readline()
'username = "umesh"\n'
f.readline()
'print(username)'
f.readline()
''
f.readline()
''
f.readline()
''

# This is with __next__ (behind the scene of python looping)

>>> f = open('chai.py')
>>> f.__next__()
'import time\n'
>>> f.__next__()
'print("Chai is here")\n'
>>> f.__next__()
'username = "umesh"\n'
>>> f.__next__()
'print(username)'
>>> f.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    f.__next__()
    ~~~~~~~~~~^^
StopIteration # this is exception and python handles it when a iterable object ends


# behind the scene of python working as iterator
>>> mylist = [1,2,3,4]
>>> I = iter(mylist)
>>> I
<list_iterator object at 0x1006040d0>   // this is reference where the next() is pointing / or iter is pointing and it always points at first memory location only
>>> I.__next__()
1
>>> I.__next__()
2
>>> I
<list_iterator object at 0x1006040d0>   // first memory location only
>>> I.__next__()
3
>>> I.__next__()
4
>>> I
<list_iterator object at 0x1006040d0>    // first memory location only
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    I.__next__()
    ~~~~~~~~~~^^
StopIteration
>>> 