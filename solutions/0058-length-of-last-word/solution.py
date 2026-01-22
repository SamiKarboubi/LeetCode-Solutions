class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        compteur = 0
        string_found = False
        for i in range(len(s)-1,-1,-1):
            if s[i] == ' ' and string_found:
                return compteur
            if s[i] != ' ':
                string_found = True
                compteur += 1
        return compteur        
                
