""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        temp = head
        new_head = None

        while temp:
            next_node = temp.next

            temp.next = temp.prev
            temp.prev = next_node

            new_head = temp
            temp = next_node

        return new_head