"""
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
def add_num(L1,L2):
    num1=0
    num2=0
    len1=0 
    len2=0
    ii=0
    while list:L1
        len1+=1
    for i in range(0,len(L1)):
        num1+=(10**i)*L1[i]
    for i in range(0,len(L2)):
        num2+=(10**i)*L2[i]
    num3=num1+num2
    listout=[]
    while(num3!=0):
        listout.append(int(num3%((10))))
        num3=(num3-num3%((10)))/10
    return listout
array1=[1,2,3]
array2=[0,1,2]
print(add_num(array1,array2))