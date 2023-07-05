# 0x06-python-classes

## Description

This project is about OOP.

Background Context

OOP is a totally new concept for all of you (especially those who think they know about it :)).

### Files

#### Mandatory Tasks

| File | Description |
| ------ | ------ |
| [0-square.py](0-square.py) | Write an empty class Square that defines a square |
| [1-square.py](1-square.py) | Write a class Square that defines a square by: (based on 0-square.py) *Private instance attribute: size* Instantiation with size (no type/value verification) * You are not allowed to import any module |
| [2-square.py](2-square.py) | Write a class Square that defines a square by: (based on 1-square.py) *Private instance attribute: size* Instantiation with optional size: def __init__(self, size=0): - size must be an integer, otherwise raise a TypeError exception with the message size must be an integer. - if size is less than 0, raise a ValueError exception with the message size must be >= 0 * You are not allowed to import any module |
| [3-square.py](3-square.py) | Write a class Square that defines a square by: (based on 2-square.py) *Private instance attribute: size* Instantiation with optional size: def __init__(self, size=0): **size must be an integer, otherwise raise a TypeError exception with the message size must be an integer** if size is less than 0, raise a ValueError exception with the message size must be >= 0 * Public instance method: def area(self): that returns the current square area |
| [4-square.py](4-square.py) | Write a class Square that defines a square by: (based on 3-square.py) *Private instance attribute: size: ** property def size(self): to retrieve it ** property setter def size(self, value): to set it: *** size must be an integer, otherwise raise a TypeError exception with the message size must be an integer ***if size is less than 0, raise a ValueError exception with the message size must be >= 0* Instantiation with optional size: def __init__(self, size=0): **Public instance method: def area(self): that returns the current square area |
| [5-square.py](5-square.py) | Write a class Square that defines a square by: (based on 4-square.py) *Private instance attribute: size: ** property def size(self): to retrieve it ** property setter def size(self, value): to set it: *** size must be an integer, otherwise raise a TypeError exception with the message size must be an integer *** if size is less than 0, raise a ValueError exception with the message size must be >= 0* Instantiation with optional size: def __init__(self, size=0): **Public instance method: def area(self): that returns the current square area** Public instance method: def my_print(self): that prints in stdout the square with the character #: ***if size is equal to 0, print an empty line |
| [6-square.py](6-square.py) | Write a class Square that defines a square by: (based on 5-square.py) *Private instance attribute: size: ** property def size(self): to retrieve it ** property setter def size(self, value): to set it: *** size must be an integer, otherwise raise a TypeError exception with the message size must be an integer *** if size is less than 0, raise a ValueError exception with the message size must be >= 0* Private instance attribute: position: **property def position(self): to retrieve it** property setter def position(self, value): to set it: ***position must be a tuple of 2 positive integers, otherwise raise a TypeError exception with the message position must be a tuple of 2 positive integers * Instantiation with optional size and optional position: def __init__(self, size=0, position=(0, 0)): * Public instance method: def area(self): that returns the current square area * Public instance method: def my_print(self): that prints in stdout the square with the character #:** if size is equal to 0, print an empty line ** position should be use by using space - Don’t fill lines by spaces when position[1] > 0|

#### Advanced Tasks

| File | Description |
| ------ | ------ |
| [100-singly_linked_list.py](100-singly_linked_list.py) | Build Linked List in python and use methods of class to handle it |
| [101-square.py](101-square.py) | same class of 6-square.py task but position should be use by using space |
| [102-square.py](102-square.py) | same class of 101-square.py task but this time use  __eq__, __ne__, __ge__, __le__, __gt__ and __lt__ magic methods  |
| [103-magic_class.py](103-magic_class.py) | convert Python bytecode of Python class MagicClass to python code |
