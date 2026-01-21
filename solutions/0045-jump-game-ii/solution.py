class Solution:
    def jump(self, nums: List[int]) -> int:
        compteur = 0
        rng = 0
        current_end = 0
        for i in range(len(nums)-1):
            rng = max(rng,i+nums[i])
            if i == current_end:
                compteur += 1
                current_end = rng
        return compteur

                




