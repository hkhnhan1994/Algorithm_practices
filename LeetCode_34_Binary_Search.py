"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""
class Solution:
    def __init__(self,nums,target):
        self.nums =nums
        self.target =target
        self.BS(0,len(nums)-1)
        print (self.BS(0,len(nums)-1))
    def BS(self,low,high):
        try:
            results=[]
            mid= high-(high-low)//2
            if self.nums[mid]==self.target:
                results.append(mid)
                if self.nums[mid]==self.nums[mid-1]:
                    results.append(mid-1)
                elif self.nums[mid]==self.nums[mid+1] and (mid+1) not in results:
                    results.append(mid+1)
                else: return [-1,-1]
                    
            elif self.nums[mid]<self.target:
                low=mid+1
                return self.BS(high,low)
            elif self.nums[mid]>self.target:
                high=mid-1
                return self.BS(low,high)
            else: return [-1,-1]
            return results
        except: return [-1,-1]
arr = [1, 1,3,4,4, 40]
x = 4
_=Solution(arr, x)      