class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = len(nums) - 1
        i = 0
        while i <= j:
            if nums[i] == val:
                while nums[j] == val and j > i:
                    j -= 1
                c = nums[i]
                nums[i] = nums[j]
                nums[j] = c
                j -= 1
            else:
                i += 1
            
        return i


                

