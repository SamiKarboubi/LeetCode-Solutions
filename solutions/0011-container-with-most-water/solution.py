class Solution:
    def maxArea(self, height: List[int]) -> int:
        j = len(height) - 1
        i = 0
        maximum = 0
        while i != j:
            minimum = min(height[i],height[j])
            water = minimum * (j-i)
            if water > maximum:
                maximum = water
            if minimum == height[i]:
                i += 1
            else:
                j -= 1
        return maximum

