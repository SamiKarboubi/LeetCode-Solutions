class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        infos = {i: "" for i in range(numRows)}
        cycle = 2*numRows - 2
        for i in range(len(s)):

            pos = i % cycle
            if pos >= numRows:
                pos = cycle - pos
            infos[pos] += s[i]

        result = ""

        for i in range(numRows):
            result += infos[i]
        
        return result

        



