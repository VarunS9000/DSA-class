max_size = 5
queue = [None]*max_size
front = -1
rear = -1

def insert(element):
    global queue
    global rear
    global front
    global max_size

    if((front ==0 and max_size-1==rear) or (front==rear+1 and queue[rear] is not None)):
        print('Queue is full')

    else:
        if front<0:
            front+=1
        rear = (rear+1)%max_size
        queue[rear] = element
        
        showCircularQueue(front,rear,max_size)



def showCircularQueue(front,rear,max_size):
    global queue
    x = []
    for i in range(front,max_size+front):
        if(i%max_size==rear):
            x.append(queue[i%max_size])
            break

        elif (queue[i%max_size] is not None):
            x.append(queue[i%max_size])

    print(x)

        
           

        


def delete():
    global rear
    global front
    global queue

    if(rear+1 == front and queue[rear] == None):
        print('You cannot delete. The queue has been re-initialized ')
        resetQueue()

    else:
        queue[front]=None
        front = (front+1)%max_size
        showCircularQueue(front,rear,max_size)
        


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
