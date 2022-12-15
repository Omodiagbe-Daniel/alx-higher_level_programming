#!/usr/bin/python3
"""defines a singly linked list"""


class Node:
    """defines the node of a singly linked list"""

    @property
    def data(self):
        """retrieve data"""
        return self.__data

    @setter.data
    def data(self, value):
        """set data to value"""
        if value is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve next_node"""
        return self.__next_node

    @setter.next_node
    def next_node(self, value):
        """set next_node to value"""
        if value is not None or not isinstance(value, Node):
            raise TypeError("next_node must be a node object")
        self.__next_node = value

    def __init__(self, data, next_node=None):
        """inasantiating"""
        self.data = data
        self.next_node = next_node


class SIngleLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """instantiating"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new node"""
        node = Node(value)
        if self.__head is None:
            node.next_node = None
            self.__head = node
        elif self.__head.data > value:
            node.next_node = self.__head
            self.__head = node
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            node.next_node = tmp.next_node
            tmp.next_node = node

    def __str__(self):
        """print the result to the standand output"""
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
