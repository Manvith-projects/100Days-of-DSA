class Solution:
    def Twosum(self,nums,target):

        numsMap={}
        for i in range(len(nums)):
            complement= target - nums[i]

            if complement in numsMap:
                return [numsMap[complement],i]

            numsMap[nums[i]]=i

        return []

sol = Solution()
print(sol.Twosum([2,7,11,15],9))