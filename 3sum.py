class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
       nums.sort()
       res = []
       for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == num:
                continue
            l = i+1
            r= len(nums)-1
            while l < r:
                if nums[l] + nums[r] + num > 0:
                    r-=1
                elif nums[l] + nums[r] + num <0:
                    l+=1
                else:
                    res.append([num,nums[l],nums[r]])
                    r-=1
                    while nums[r]==nums[r+1] and l <r:
                        r-=1 
       return res
                    
