class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
             return []
    
        # Liste des lettres correspondant aux chiffres 2-9
        phone = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    
    # Initialisation avec une chaîne vide
        result = [""]
    
        for digit in digits:
        # Obtenir les lettres correspondant au chiffre actuel
            letters = phone[int(digit) - 2]
            new_result = []
        
        # Étendre chaque combinaison actuelle avec les lettres du chiffre actuel
            for combination in result:
                  for letter in letters:
                       new_result.append(combination + letter)
        
        # Mettre à jour le résultat avec les nouvelles combinaisons
            result = new_result
    
        return result


            
        


        
