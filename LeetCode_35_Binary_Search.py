class Solution:
    def __init__(self,nums,target):
        self.nums = nums
        self.target = target
    def BS(self,high,low):
        try:
            mid= high-(high-low)//2
            if self.nums[mid]==self.target:
                return mid
            elif self.nums[mid]<self.target:
                low=mid+1
                return self.BS(high,low)
            else:
                high=mid-1
                return self.BS(high,low)
        except:

            return mid 
array=[1,2,4,7,11,13,20,28,39]
result=Solution(array,40)
print(result.BS(len(array)-1,0)) 
    
