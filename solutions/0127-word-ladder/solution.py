import string
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        n = len(beginWord)
        alphabet = list(string.ascii_lowercase)
        visited = set([beginWord]) 
        i = 1 
        queue = deque([(beginWord,i)]) 

        while queue: 
            w,steps = queue.popleft()  
            
            if w == endWord:
                return steps

            for i in range(n):
                for a in alphabet:
                    if w[i] != a:
                        newWord = w[:i] + a + w[i+1:]
                        if newWord in wordList and newWord not in visited:
                            visited.add(newWord)
                            queue.append((newWord,steps+1))
        return 0
