class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ''

        cnt_t = {}
        window = {}

        for i in range(len(t)):
            cnt_t[t[i]] = cnt_t.get(t[i], 0) + 1

        have = 0
        need = len(cnt_t)

        left = 0
        mini = float('inf')
        res = ''

        for right in range(len(s)):
            ch = s[right]
            window[ch] = window.get(ch, 0) + 1

            if ch in cnt_t and window[ch] == cnt_t[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < mini:
                    mini = (right - left + 1)
                    res = s[left : right + 1]

                ch = s[left]
                window[ch] -= 1

                if ch in cnt_t and window[ch] < cnt_t[ch]:
                    have -= 1

                left += 1

        return res

