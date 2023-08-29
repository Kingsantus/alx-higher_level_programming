#!/usr/bin/python3
"""Node Module"""

class Node:
    """node class"""
    def __init__(self, data, next_node=None):
        """initializing an instance"""
        self.data = data
        self.next_node = next_node
    """setter attribute method"""
    @property
    def data(self):
        return self.__data

    """getter attribute method"""
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    """setter attribute method"""
    @property
    def next_node(self):
        return self.__next_node

    """getter attribute method"""
    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singlelinkedlist class"""
    def __init__(self):
        self.head = None

    """checking and initializing a single linked list"""
    def sorted_insert(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        elif value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            """tranversing through the list"""
            while current.next_node is not None and value > current.next_node.data:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    """appending a new node to the list"""
    def __str__(self):
        nodes = []
        current = self.head
        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node
        return "\n".join(nodes)

