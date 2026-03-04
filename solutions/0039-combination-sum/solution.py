class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        n = len(candidates)
        result = []
        def helper(candidat,j,current_sum):

            if sum(candidat) == target:
                result.append(list(candidat))
                return
            for i in range(j,n):
                if current_sum + candidates[i] > target:
                    break
                candidat.append(candidates[i])
                helper(candidat,i,current_sum+candidates[i])
                candidat.pop()

        helper([],0,0)
        return result



        
