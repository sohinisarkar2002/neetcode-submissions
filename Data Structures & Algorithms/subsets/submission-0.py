class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if i == len(nums):
                # sol[:] instead of sol -> to store a copy of sol in res
                res.append(sol[:])
                return

            # Not Take
            backtrack(i + 1)

            # Take
            sol.append(nums[i])
            backtrack(i + 1)
            sol.pop()
        
        backtrack(0)

        return res