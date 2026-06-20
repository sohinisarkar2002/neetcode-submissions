class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans, sol = [], []

        def backtrack(x):
            if len(sol) == k:
                ans.append(sol[:])
                return

            left_to_pick = x
            still_need = k - len(sol)

            # Not Pick
            if left_to_pick > still_need:
                backtrack(x - 1)
            
            # Pick
            sol.append(x)
            backtrack(x - 1)
            sol.pop()

        backtrack(n)

        return ans