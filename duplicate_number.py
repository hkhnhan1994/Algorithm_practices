"""
find duplicate number from array and print the it out the console
the value element of array is lesther than total member of the array
"""
# Method 1
# def findDuplicateNumber(nums):
#     Totoire =nums[0]
#     hare=nums[0]
#     while True:
#         Totoire=nums[Totoire]
#         hare=nums[nums[hare]]
#         if Totoire==hare:
#             break
#     ptr1=nums[0]
#     ptr2=Totoire
#     while ptr1 != ptr2:
#         ptr1=nums[ptr1]
#         ptr2=nums[ptr2]
#     return ptr1

# print(findDuplicateNumber([1,5,2,3,5,4]))

#Method 2

def findDuplicateNumber(nums,cmp):
    Dup=False
    numdup=0
    list_duplicates=[]
    for i in range(0,len(nums)):
        if i == cmp:
            continue
        if nums[i] == nums[cmp]:
          numdup=nums[cmp]
          Dup=True
          break
    if Dup:
        list_duplicates.append(numdup)
    if cmp+1 <len(nums):
        list_duplicates+= findDuplicateNumber(nums,cmp+1)
    return list_duplicates
print(findDuplicateNumber([2,3,1,5,3,1],0))