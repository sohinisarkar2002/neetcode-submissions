class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r, maxf, maxlen = 0, 0, 0, 0
        hmap = {}

        while r < len(s):
            if s[r] not in hmap:
                hmap[s[r]] = 0
            hmap[s[r]] += 1

            maxf = max(maxf, hmap[s[r]])

            diff = (r - l + 1) - maxf

            while diff > k:
                hmap[s[l]] -= 1
                l += 1
                diff = (r - l + 1) - maxf
            
            if diff <= k:
                maxlen = max(maxlen, r - l + 1)

            r += 1
        
        return maxlen