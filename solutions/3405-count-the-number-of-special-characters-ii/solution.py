class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        
        lower_hash = {}
        upper_hash = {}

        for idx,c in enumerate(word):
            if c.islower():
                lower_hash[c] = idx
            if c.isupper() and c not in upper_hash:
                upper_hash[c] = idx

        counter = 0
        for upper_char in upper_hash.keys():
            upper_char_lower = upper_char.lower()
            if upper_char_lower in lower_hash and lower_hash[upper_char_lower] < upper_hash[upper_char]:
                counter += 1
        return counter
        
