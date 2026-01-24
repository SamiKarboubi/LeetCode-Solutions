class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        string_found = False

        for i in range(len(s) - 1, -1, -1):
            if (s[i] == ' ' and string_found):
                result.append(s[i+1:index+1])
                string_found = False
            if s[i] != ' ' and not string_found:
                string_found = True
                index = i
            if i == 0 and string_found:
                result.append(s[i:index+1])
        return " ".join(result)
