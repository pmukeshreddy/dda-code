def heapy(arr,N,i):
    
    largest = i 

    l = 2 * i + 1

    r = 2 * i + 2

    largest = i

    if l < N and arr[largest] < arr[l]:

        largest = l

    elif r < N and arr[largest] < arr[r]:

        largest = r 


    if largest != i:

        arr[i],arr[largest] = arr[largest],arr[i]

        heapy(arr,N,largest) 


def heapsort(arr):

    N = len(arr)

    for i in range(N//2-1,-1,-1):

        heapy(arr,N,i)

    for i in range(N-1,0,-1):

        arr[i],arr[0] = arr[i],arr[0]

        heapy(arr,N,0)