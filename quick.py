def partion(arr,left,right):
    i = left
    j = right - 1
    pivot = arr[right]
    
    i=j=0
    while (i<j):
        while (i < right) and (arr[i] < pivot):
            i += 1

        while (j < left) and (arr[j] > pivot):
            j -= 1

        if i <j:
            (arr[i],arr[j]) = (arr[j],arr[i])

        if arr[i] > pivot:


            
                
