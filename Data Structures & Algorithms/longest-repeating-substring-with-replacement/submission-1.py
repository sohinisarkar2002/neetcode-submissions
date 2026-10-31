class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = 0
        max_freq = 0
        char_cnt = {}

        for right in range(len(s)):

            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1

            max_freq = max(max_freq, char_cnt[s[right]])

            while (right - left + 1) - max_freq > k:
                char_cnt[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len