from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        l = defaultdict(int)

        for n in nums:
            l[n] += 1
            
        maxi = float('-inf')
        ans = 0
        for k, v in l.items():
            if maxi < v:
                maxi = max(maxi, v)
                ans = k

        return ans