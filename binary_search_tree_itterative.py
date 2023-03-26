def bst(list,key):
    low = 0
    high = len(list) - 1
    while low<=high:
        mid = (low+high)//2

        if list[mid] < key:
            low = mid + 1
        elif list[mid] > key:
            high = mid - 1
        else:
            return mid        
    return -1

    
list = [1,2,3,4,5]
bst(list,4)
print(bst(list,3))