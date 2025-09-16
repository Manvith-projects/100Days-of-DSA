#problem 344 
# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]


from typing import List
class Solution:
    def ReverseString(self,s:List[str])-> None:

        left,right=0,len(s)-1

        while left<right:
            s[left],s[right]=s[right],s[left]

            left+=1
            right-=1

        return s

sol=Solution()

print(sol.ReverseString(["h","e","l","l","o"]))
