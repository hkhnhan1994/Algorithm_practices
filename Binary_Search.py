class BinarySearch:
    def __init__(self,nums,target):
        self.nums=nums
        self.target=target
        # return self.BS(0,len(nums)-1)
        
    def BS(self,lowpoint,highpoint):

        while lowpoint <= highpoint:
            midpoint = highpoint-(highpoint-lowpoint)//2
            if self.nums[midpoint]<self.target:
                lowpoint =midpoint+1
            elif self.nums[midpoint]>self.target:
                highpoint =midpoint-1
            else:
                return midpoint
    def BS_recursion(self,lowpoint,highpoint):

            midpoint = highpoint-(highpoint-lowpoint)//2
            if self.nums[midpoint]<self.target:
                lowpoint =midpoint+1
                return self.BS_recursion(lowpoint,highpoint)
            elif self.nums[midpoint]>self.target:
                highpoint =midpoint-1
                return self.BS_recursion(lowpoint,highpoint)
            else:
                return midpoint
arr = [2, 3,4, 10, 40]
x = 4
_=BinarySearch(arr, x)
print(_.BS_recursion(0 ,len(arr)-1))
print(_.BS(0 ,len(arr)-1))