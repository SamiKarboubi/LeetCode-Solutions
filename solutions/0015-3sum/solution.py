class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        for k in range(n):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                s = nums[k] + nums[i] + nums[j]
                if s == 0:
                    result.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif s < 0:
                    i += 1
                else:
                    j -= 1
        return result
