def calc_ave(ls):
    total=sum(ls)
    ave=total/len(ls)

    return ave



test=[int(x) for x in input("Enter the values separated by spaces to calculate Average: ").split()]

print("The average for",test,"is:",calc_ave(test))
