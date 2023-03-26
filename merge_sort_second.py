def mergesort(array):

    if len(array) > 1:

        r = len(array)//2
        L = array[:r]
        R = array[r:]

        mergesort(L)
        mergesort(R)

        i=j=k=0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            array[k] = R[j]
            j += 1     
            k += 1

    return array        

def print_list(arr):
    for i in range(len(arr)):
        print(arr[i])


arr = [23,12,1,2,6]
print_list(mergesort(arr))