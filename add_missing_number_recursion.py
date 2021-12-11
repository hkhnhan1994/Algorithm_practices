

def recursionPlus1(start,end):
    elements =[]
    elements.append(start)
    if start is not end:
        elements+=recursionPlus1(start+1,end)
    return elements
def insert_miss_num(elements):
    new_element=[]
    
    for i in range(1,len(elements)):
        new_element+=recursionPlus1(elements[i-1],elements[i])
    return new_element
if __name__=="__main__":
   elements=[1,5,8] 

   print( insert_miss_num(elements))