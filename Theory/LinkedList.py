class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node1.next = node2
node2.next = node3
# print(node1.data)   
# print(node2.data)
# print(node3.data)

head= node1
def insert_node(data,pos,head):
    new_node = Node(data)
    len = 0
    perm_head = head
    while head!= None:
        len+=1
        if head.next ==None:
            last_node=head
        head = head.next
    head = perm_head
    if pos==1:
        new_node.next = head
        perm_head = new_node
        return perm_head
    elif pos>len:
        last_node.next = new_node
        return perm_head
    else:
        curr=1
        while curr<pos-1:
            head = head.next
            curr+=1
        temp = head.next
        head.next=new_node
        new_node.next=temp
        return perm_head
    
def delete(pos,head):
    len = 0
    perm_head=head
    while head!= None:
        len+=1
        if head.next ==None:
            last_node=head
        head = head.next
    head = perm_head
    if pos==1:
        perm_head=head.next
        return perm_head
    elif pos>len:
        return perm_head
    else:
        curr=1
        while curr<pos-1:
            head = head.next
            curr+=1
        head.next=head.next.next
        return perm_head
def print_ll(head):
    while head is not None:
        print(head.data)
        head=head.next
    return 



head = insert_node(11,1,head)
head = delete(2,head)
print_ll(head)

