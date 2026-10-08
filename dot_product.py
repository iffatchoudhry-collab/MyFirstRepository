def main():
    list_1 = [2, 7, 4, 6, 2]
    list_2 = [1, 6, 3, 5, 1]
    
 
    def calc_dot_product(ls1,ls2):
        i=0
        j=0
        dot_product=0
        while i<len(ls1) and j<len(ls2):
            dot=ls1[i]*ls2[j]
            i+=1
            j+=1
            dot_product+=dot
       
    #####################
        return dot_product
 
 
    # Example usage
    
    result = calc_dot_product(list_1, list_2)
    print("The Dot Product of these two lists is:", result)
    
main()