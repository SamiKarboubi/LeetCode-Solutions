class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        current = strs[0]
        for i in range(len(current)):
            for word in strs:
                if i >= len(word) or word[i] != current[i]:
                    return current[:i]
        return current

        
