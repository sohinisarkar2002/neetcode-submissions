class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1

        for k, v in hmap.items():
            if v > 1:
                return True

        return False