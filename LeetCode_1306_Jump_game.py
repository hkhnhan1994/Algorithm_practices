"""
Given an array of non-negative integers arr, you are initially positioned at start index of the array. 
When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

Notice that you can not jump outside of the array at any time.

Example 1:

Input: arr = [4,2,3,0,3,1,2], start = 5
Output: true
Explanation: 
All possible ways to reach at index 3 with value 0 are: 
index 5 -> index 4 -> index 1 -> index 3 
index 5 -> index 6 -> index 4 -> index 1 -> index 3 
Example 2:

Input: arr = [4,2,3,0,3,1,2], start = 0
Output: true 
Explanation: 
One possible way to reach at index 3 with value 0 is: 
index 0 -> index 4 -> index 1 -> index 3
Example 3:

Input: arr = [3,0,2,1,2], start = 2
Output: false
Explanation: There is no way to reach at index 1 with value 0.
 

Constraints:

1 <= arr.length <= 5 * 104
0 <= arr[i] < arr.length
0 <= start < arr.length
"""
class Solution:
    def __init__(self,nums, start):
        self.nums = nums
        self.visited=[]
        self.queue=[]
        self.visited.append(start)
        self.queue.append(start)
        self. result=[]
    def BFS(self):
        if self.queue is not None:
            val=self.queue.pop(0)
            self.result.append(val)
            if self.nums[val]==0:
                # print(f"{val} have value :{self.nums[val]}",end=" ")
                return self.result
            adjacency=[val+self.nums[val],val-self.nums[val]]
            # print(val,end=" ")
            


        for i in adjacency:
            if i <= (len(self.nums)-1) and i>0:
                self.visited.append(i)
                self.queue.append(i)
        return self.BFS()

arr = [4,2,3,0,3,1,2]
start = 5
_=Solution(arr,start)
print(_.BFS())