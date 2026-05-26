class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        hashmap = {}
        word = set(word)
        counter = 0
        for c in word:
            if c.lower() in hashmap:
                hashmap[c.lower()] += 1
                if hashmap[c.lower()] >= 2:
                    counter += 1
            else:
                hashmap[c.lower()] = 1

        return counter
        
