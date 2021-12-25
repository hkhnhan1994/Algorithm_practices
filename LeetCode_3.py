"""
Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""
def lengthOfLongestSubstring(s):

        Str=[]
        _len=0
        numbig=0
        for char in s:
                Str.append(char)
                _len+=1
        highest=0
        i=0
        for c in range(0, _len):
                i=c+1
                getchar=[]
                getchar.append(Str[c])
                count=1
                while i< _len:
                                       
                        if Str[i] in getchar:
                                break
                        else: 
                                getchar.append(Str[i])
                                count+=1
                        i+=1
                        
                if highest<count: highest=count
        return highest
def lengthOfLongestSubstring2(s: str) -> int:
		res = 0
		ls = ""   #longest substring
		for c in s:
			if c in ls:
				res = max(res,len(ls))
				ls = ls[ls.find(c)+1:] + c
			else:
				ls += c
		res = max(res,len(ls))
		return res
arr="abcddccd"
print(lengthOfLongestSubstring2(arr))
