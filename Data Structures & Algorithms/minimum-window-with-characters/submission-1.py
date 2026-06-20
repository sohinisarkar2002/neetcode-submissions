from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n, m = len(s), len(t)
        minlen = float('inf')
        l, r, cnt, start = 0, 0, 0, -1
        hmap = defaultdict(int)

        for i in range(m):
            hmap[t[i]] += 1

        while r < n:
            if hmap[s[r]] > 0:
                cnt += 1
            hmap[s[r]] -= 1

            while cnt == m:
                if (r - l + 1) < minlen:
                    minlen = r - l + 1
                    start = l
                hmap[s[l]] += 1
                if hmap[s[l]] > 0:
                    cnt -= 1
                l += 1

            r += 1

        if start == -1:
            return ""
        else:
            return s[start : (start + minlen)]

