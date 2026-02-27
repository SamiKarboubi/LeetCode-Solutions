from collections import deque

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        bank = set(bank)
        if endGene not in bank:
            return -1
        
        genes = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        
        while queue:
            current, steps = queue.popleft()
            
            if current == endGene:
                return steps
            
            for i in range(8):
                for g in genes:
                    if current[i] != g:
                        mutated = current[:i] + g + current[i+1:]
                        
                        if mutated in bank and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, steps + 1))
        
        return -1
            
