''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        # ans = [[],[]]
        # if not head:
        #     return ans
        
        # temp = head
        
        # while temp:
        #     ans[0].append(temp.data)
        #     temp = temp.next
            
        # temp = head
        
        # while temp.next:
        #     temp = temp.next
            
        # while temp:
        #     ans[1].append(temp.data)
        #     temp = temp.prev
            
        # return ans
            
        
        
        ans = [[], []]

        if not head:
            return ans

        temp = head

        while temp.next:
            ans[0].append(temp.data)
            temp = temp.next

        ans[0].append(temp.data)

        while temp:
            ans[1].append(temp.data)
            temp = temp.prev

        return ans