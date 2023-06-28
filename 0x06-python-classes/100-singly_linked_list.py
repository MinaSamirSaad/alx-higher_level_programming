#!/usr/bin/python3
''' module100-singly_linked_list.py creates Node class '''


class Node:
    ''' Node class doc '''
    def __init__(self, data, next_node=None):
        ''' constructor doc '''
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        ''' get size '''
        return self.__data

    @data.setter
    def data(self, value):
        ''' data setter '''
        if type(value) is not int:
            raise TypeError('size must be an integer')
        self.__data = value

    @property
    def next_node(self):
        ''' get next node '''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        ''' next node setter '''
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    ''' single linked list class'''
    def __init__(self):
        ''' constructor '''
        self.__head = None

    def sorted_insert(self, value):
        ''' replace __str__'''
        temp = self.__head
        if temp is None:
            n = Node(value)
            self.__head = n
            return

        if temp.data > value:
            n = Node(value)
            n.next_node = temp
            self.__head = n
            return

        while temp.next_node is not None:
            if temp.next_node.data > value:
                break
            temp = temp.next_node
        n = Node(value)
        n.next_node = temp.next_node
        temp.next_node = n
        return

    def __str__(self):
        ''' print all data in linked list '''
        temp = self.__head
        while temp.next_node is not None:
            print(str(temp.data))
            temp = temp.next_node
        return f'{str(temp.data)}'
