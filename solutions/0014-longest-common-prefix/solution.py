class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        current = strs[0]
        remaining = strs[1:]
        i=0
        while i<len(current):
            for word in remaining:
                if i >= len(word) or word[i] != current[i]:
                    return result
            result += current[i]
            i += 1 
        return result

        

