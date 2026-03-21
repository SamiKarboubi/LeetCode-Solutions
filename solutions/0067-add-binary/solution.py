class Solution:
    def addBinary(self, a: str, b: str) -> str:

        result = []

        i = len(a)-1
        j = len(b)-1
        r = 0

        while i >= 0 or j >= 0 or r:
            
            total = r

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            r = total // 2

        return "".join(result[::-1])
