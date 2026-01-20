class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        j = 0
        candidat = None
        for i in range(len(nums)):
            if j == 0:
                candidat = nums[i]
            j += 1 if nums[i] == candidat else -1
        return candidat


    

