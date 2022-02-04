data = [1,2,3,4,5,6,7,8,9]

def linearSearch(data,ele):
    found = False
    for i in range(len(data)):
        if ele == data[i]:
            found = True
            print('Element Found at position ',i+1)


    if not found:
        print('Element not in the list')



def binarySearch(data,start,end,ele):
    if end>=start:
        mid = (end+start)//2

        if(data[mid] == ele):
            print('Element found at position',mid+1)

        elif(ele<data[mid]):
            
            binarySearch(data,start,mid-1,ele)

        elif(ele>data[mid]):
            binarySearch(data,mid+1,end,ele)

    else:
        print('Element not in the list')

linearSearch(data,6)
binarySearch(data,0,len(data)-1,6)

        



            

        
        
