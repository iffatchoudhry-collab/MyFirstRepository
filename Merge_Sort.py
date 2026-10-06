def split(ls):
    if len(ls)<=1:
        return ls

    #Divide the list in 2 almost equal parts

    mid=len(ls)//2
    left_ls=ls[:mid]
    right_ls=ls[mid:]

    #sort both halves

    left_sorted=split(left_ls)
    right_sorted=split(right_ls)


    #merge the sorted halves

    return combine(left_sorted,right_sorted)

def combine(left,right):
    sorted_list=[]
    l=0
    r=0

    while l<len(left) and r<len(right):
        if left[l]<right[r]:
            sorted_list.append(left[l])
            l+=1
        else:
            sorted_list.append(right[r])
            r+=1

    sorted_list.extend(left[l:])
    sorted_list.extend(right[r:])

    return sorted_list




ls1=[34,55,63,78,12,45,90,24]

print("original List is: ",ls1)

sorted_list=split(ls1)

print("Sorted List is: ",sorted_list)
