def search(list,low, high,key):


    if high >= low:

        mid = (high+low)//2

        if list[mid] == key:
            return mid
        elif list[mid] > key:
            return search(list,low,mid-1,key)
        elif list[mid] < key:
            return search(list,mid + 1,high,key)
    else:
        return -1      

list = [4,5,6,90] 

print(search(list,0,3,90))