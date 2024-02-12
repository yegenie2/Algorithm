import sys

t = int(input())
stack = []
def push(num):
    stack.append(num)

def pop():
    if len(stack) == 0:
        print(-1)
    else:
        print(stack[-1])
        stack.pop()

def size():
    print(len(stack))

def empty():
    if len(stack) == 0:
        print(1)
    else :
        print(0)

def top():
    if len(stack) == 0:
        print(-1)
    else :
        print(stack[-1])

for i in range(t):
    
    msg = sys.stdin.readline().split()

    if msg[0] == 'push':
        push(int(msg[1]))
    elif msg[0] == 'top':
        top()
    elif msg[0] == 'size':
        size()
    elif msg[0] == 'empty':
        empty()
    elif msg[0] == 'pop':
        pop()