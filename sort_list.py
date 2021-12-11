import numpy as np
import random
newarray=random.sample(range(0,20),5)
print(newarray)

# sort by descending
def sort_method(nums,dir='asc'):
    sort_array=[]
    copy_array=nums
    while copy_array!=[]:
        if dir=='desc':
            sort_array.append(max(copy_array))
            copy_array.remove(max(copy_array))
        elif dir=='asc':
            sort_array.append(min(copy_array))
            copy_array.remove(min(copy_array))
    return sort_array

print(sort_method(newarray),'desc')
