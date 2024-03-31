class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = {}
        for num in nums:
            if num in bucket.keys():
                bucket[num] +=1
            else:
                bucket[num] =1
        sorted_bucket = sorted(bucket.items(), key = lambda kv:kv[1],reverse = True)
        res = []
        #res.append(len(sorted_bucket))
        for n, c in sorted_bucket:
            if k <= 0:
                return res
            else:
                k-=1
            res.append(n)
        return res