class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        last_index = {}
        l = 0
        max_len = 0
        for r in range(len(s)):
            if s[r] in last_index and last_index[s[r]] >= l:
                l = last_index[s[r]] + 1         
            last_index[s[r]] = r
            max_len = max(max_len,r - l + 1)
        return max_len
        

