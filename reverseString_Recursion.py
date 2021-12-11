class Solution:
    def __init__(self,nums):
        self.nums = nums
        self.execute=[]
        self.reverseString(nums)
        
    def reverseString(self,s):
        
        if s != []:
            self.execute.append(s[len(s)-1])
            s=s[:-1]
            self.reverseString(s)

        
word=["h","e","e","l"]

re=Solution(word)
print(re.execute)
