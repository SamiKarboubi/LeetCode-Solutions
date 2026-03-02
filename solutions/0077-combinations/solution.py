class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
        self.result = []
        
        def helper(comb,j):

            if len(comb) == k:
                
                self.result.append(list(comb))
                return 
            
            for i in range(j,n+1):
                
                comb.append(i)
                helper(comb,i+1)
                comb.pop()    
        helper([],1)

        return list(self.result)
            

        
