class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        
        res = []
        sub = []
        def backtrack(i):
            if i >= len(nums):
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()
            backtrack(i+1)

        backtrack(0) 

        return res

