# 7. Reverse Integer
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes 
# the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


class Solution:
    @staticmethod
    def ReverseInteger(x):
        sign = -1 if x<0 else 1
        x=abs(x)

        if x==0:
            return 0
        new=[]
        while x!=0:
            temp=x%10
            new.append(str(temp))
            x=x//10
        
        ans=int("".join(new))*sign
        if ans < -2**31 or ans > 2**31 - 1:
            return 0 


        return ans

print(Solution.ReverseInteger(123))
print(Solution.ReverseInteger(-123))
