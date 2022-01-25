max_size = 5
top_index = -1
stack = [None]*max_size



def push(element):
    global top_index
    global stack
    global max_size
    if(top_index+1<max_size):
        top_index+=1
        stack[top_index] = element
        print(stack[:top_index+1])

    else:
        print('Stack Overflow')


def pop():
    global top_index
    global stack
    global max_size
    if(top_index>=0):
        stack[top_index] = None
        top_index-=1
        print(stack[:top_index+1])
    else:
        print('Stack underflow')


def multipop(iterations):
    global max_size
    global stack
    if(iterations>len(stack)):
        print('This operation will cause stack underflow')

    else:
        for i in range(iterations):
            pop()
        


def showTop(stack):
    global top_index
    print(stack[top_index])

while(True):
    print("Select any of the following operations\n1. Push element\n2. Pop element\n3. Multipop element\n4. Show stack top\n PRESS 9 to QUIT")

    x = int(input('Enter option number'))

    if(x==1):
        e = int(input('Enter element to be pushed'))
        push(e)

    elif(x==2):
        pop()

    elif(x==3):
        num = int(input('Enter the number of time you want to pop the element'))
        multipop(num)

    elif(x==4):
        showTop(stack)

    elif(x==9):
        break

    else:
        print('Enter valid input')
