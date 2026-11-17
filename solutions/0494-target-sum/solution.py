class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        g_set = {0:1}
        for i in range(len(nums)):
            c_set = {}
            for key, val in g_set.items():
                c_set[key + nums[i]] = c_set.get(key + nums[i],0) + val
                c_set[key - nums[i]] = c_set.get(key - nums[i],0) + val
            g_set = c_set
        return g_set.get(target,0)


        

