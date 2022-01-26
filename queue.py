max_size = 5
queue = [None]*max_size
front = -1
rear = -1

def insert(element):
    global queue
    global rear
    global front

    if(max_size-1>rear):
        if front<0:
            front+=1
        rear+=1
        queue[rear] = element
        print(queue[front:rear+1])

    else:
        print('Queue is full')
        

   


def delete():
    global rear
    global front
    global queue

    if(rear<0 or front>rear ):
        print('Cannot delete')

    else:
        queue[front]=None
        front+=1
        print(queue[front:rear+1])


def resetQueue():
    global queue
    global front
    global rear
    global max_size

    max_size = 5
    queue = [None]*max_size
    front = -1
    rear = -1


while(True):
    print('Select option\n1. Insert element\n2. Delete\n3. Reset\n PRESS 9 TO QUIT')
    x = int(input('Enter option'))

    if(x==1):
        e = int(input('Enter element'))
        insert(e)

    elif(x==2):
        delete()

    elif(x==3):
        resetQueue()

    elif(x==9):
        break

    else:
        print('Enter valid input')
        
