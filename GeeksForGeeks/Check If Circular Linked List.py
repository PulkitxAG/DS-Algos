#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        if not head:
            return False
            
        temp = head.next
        
        while temp != head and temp is not None:
            temp = temp.next
        
        return temp == head