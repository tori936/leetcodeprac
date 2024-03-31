from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        suffix=[1]
        prefix=[1]
        lhs = 1
        rhs = 1
        for i in range(len(nums)-1,0, -1):
            rhs = rhs*nums[i]
            suffix.append(rhs)
        suffix.reverse()
        print("suffix =",suffix)
        for i in range(0,len(nums)-1,+1):
            lhs = lhs*nums[i]
            prefix.append(lhs)
        print("prefix =",prefix)
        for i in range(len(nums)):
            nums[i] = prefix[i]*suffix[i]
        return nums
tester1 = Solution()
print(tester1.productExceptSelf([1,2,3,4]))