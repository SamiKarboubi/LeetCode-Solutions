class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        dict_t = {}
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1

        dict_s = {}
        required = len(dict_t)
        formed = 0

        left = 0
        min_len = float("inf")
        res = ""

        for right in range(len(s)):
            c = s[right]
            dict_s[c] = dict_s.get(c, 0) + 1

            if c in dict_t and dict_s[c] == dict_t[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    res = s[left:right+1]

                left_char = s[left]
                dict_s[left_char] -= 1

                if left_char in dict_t and dict_s[left_char] < dict_t[left_char]:
                    formed -= 1

                left += 1

        return res
