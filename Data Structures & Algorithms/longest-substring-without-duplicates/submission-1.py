class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        char_idx = {}

        for right in range(len(s)):
            if s[right] in char_idx:
                left = max(left, char_idx[s[right]] + 1)
            
            char_idx[s[right]] = right

            max_len = max(max_len, right - left + 1)

        return max_len