class Solution:
    def __init__(self,s):
        self.s = s
        self.execute=[]
        self.swapPairs(0)
    def swapPairs(self, head):
        if (head +1) <= len(self.s):
            self.execute.append(self.s[head+1])
            self.execute.append(self.s[head])
            self.swapPairs(head+2)


r=[1,2,3,4]
x=Solution(r)
print(x.execute)