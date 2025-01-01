class Solution(object):
    def lengthOfLongestSubstring(self, s):
        l = [[]]
        i = 0
        for car in s:
            if car in l[i]:
                l.append(l[i][l[i].index(car)+1:])
                i+=1
            l[i].append(car)
        return max(len(sl) for sl in l)

                
            
            
