def two_sum(nums,target):
     for idx,ele in enumerate(nums):
                if (target-ele in nums) and(nums.index(target-ele)!=idx ):
                    return [idx,nums.index(target-ele)]

array=[3,2,4]
print(two_sum(array,6))