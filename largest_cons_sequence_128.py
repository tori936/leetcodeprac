from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        longest_len = 0
        for num in set_nums:
            curr_len = 1
            if not (num -1 in set_nums):
                while num +1 in set_nums:
                    num +=1
                    curr_len+=1
                if curr_len > longest_len:
                    longest_len = curr_len
        return longest_len 
