stack=[0]*100
size_of_stack=100
top=-1
def push(x):
    global top
    if stack_overflow():
        return "Stack Overflow"
    else:
        top+=1
        stack[top]=x
    return
def pop():
    global top
    if stack_underflow():
        return "Stack Underflow"
    else:
        top-=1
    return
def peek():
    global top
    if stack_underflow():
        return "Stack Underflow"
    else:
        return stack[top]
def stack_overflow():
        global size_of_stack
        global top
        if top==size_of_stack-1:
            return True
        else:            
            return False
def stack_underflow(): 
     global top
     if top==-1:
            return True
     else:
            return False
push(1)
push(2)
push(3)
print(stack)
pop()
print(peek())
peek()
