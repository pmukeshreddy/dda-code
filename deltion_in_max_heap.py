def heaify(arr,n,i):

    largest = i
    l = i * 2 + 1
    r = i * 2 + 2
    
    if (l < n and arr[l] > arr[largest]):
        largest = l

    if (r < n and arr[r] > arr[largest]):
        largest = r    

    if (largest != i):
        (arr[i],arr[largest]) = (arr[largest],arr[i])

        heaify(arr,n,largest)


def delete_rootnode(arr):
    global n
    last_element = arr[n-1]
    arr[0] = last_element
    n = n-1
    heaify(arr,n,0)

def printarray(arr,N):

    for i in range(N):
        print(arr[i])
    print()        


arr = [23,12,11,10,8,6]
n = len(arr)
delete_rootnode(arr)
printarray(arr,n)
