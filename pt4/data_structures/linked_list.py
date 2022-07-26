class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, nodes = None):
        self.head = None
        if nodes:
            node = Node(data=nodes.pop())
            self.head = node
            for n in nodes:
                node.next = Node(data=n)
                node = node.next

    def insert_head(self, node):
        node.next = self.head
        self.head = node

    def insert_after(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')
        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception('Node with data "%s" not found' % target_node_data)

    def insert_before(self, target_node_data, new_node):
        if not self.head:
            raise Exception('List is empty')
        if self.head.data == target_node_data:
            return self.insert_head(new_node)
        
        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception('Node with data "%s" not found' % target_node_data)

    def insert_tail(self, node):
        if not self.head:
            self.head = node
            return
        for n in self:
            pass
        n.next = node

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception('Node with data "%s" not found' % target_node_data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(str(n) for n in nodes)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

import random

rndm = []
for i in range(10):
    rndm.append(random.randint(1,50))
ll = LinkedList(rndm)
print(ll)

from collections import deque
dq = deque('abcdefghijklmnopqrstuvwxyz')
print(dq)

ll2 = LinkedList([5, 4, 3, 2, 1])
print(ll2)