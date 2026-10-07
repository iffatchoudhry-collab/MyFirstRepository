def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key

#example 
test_arr=[9,5,2,7,3]
insertion_sort(test_arr)
print("Sorted List is" \
" ",test_arr)