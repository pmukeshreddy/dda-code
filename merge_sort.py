def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]
        #recurion
        merge_sort(left_arr)
        merge_sort(right_arr)
        #merge
        i=0 #left_arry_ind
        j=0 #right_arry_ind
        k=0 #meged arry ind
        while (i<len(left_arr)) and (j<len(right_arr)):
            if left_arr[i]<right_arr[j]:
                arr[k] = left_arr[i]
                ++i
            else:
                arr[k] = right_arr[j]
                ++j
            ++k        
        while i < len(left_arr):
            arr[k] = left_arr[i]
            ++i
            ++k
        while j < len(right_arr):
            arr[k] = right_arr[j]
            ++j
            ++k
arr_test = [2,5,6,7,3,56,35]
merge_sort(arr_test)
print(arr_test)


