''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        new_node = Node(0)
        new_node.next = head

        temp = new_node

        while temp.next and temp.next.next:
            first = temp.next
            second = first.next

            first.next = second.next
            second.next = first
            temp.next = second

            temp = first

        return new_node.next