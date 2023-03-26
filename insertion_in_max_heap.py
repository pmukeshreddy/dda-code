def heapify(arr,n,i):
    parent = int(((i-1)/2))
    if arr[parent]>0:
        if arr[i] >arr[parent]:
            arr[i],arr[parent] = arr[parent],arr[i]
            heapify(arr,n,parent)

n = 0
def insert_node(arr,key):
    n +=1
    arr.append(key)
    heapify(arr,n,n-1)
def print_array(arr,n):
    for i in range(n):
        print(arr[i])
        
arr = [34,5,6,1,2,3,4]
insert_node(arr,12)
print_array(arr,6)
