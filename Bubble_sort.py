def bubble_sort(ls):
    lsn=len(ls)
    #loop through all list items
    for item in range(lsn):
        for j in range(0,lsn-item-1):
            if ls[j]>ls[j+1]:
                ls[j],ls[j+1]=ls[j+1],ls[j]

    return ls



unsorted=[9,3,55,23,12,11,19,94,97,89,78,7,8,6,99,786,911,1234,1]
print("Unsorted list is",unsorted)
print()
print("Sorted List is: ",bubble_sort(unsorted))