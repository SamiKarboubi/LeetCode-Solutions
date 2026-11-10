class Solution:
    def equationsPossible(self, equations: list[str]) -> bool:

        parent_dict = {c: c for c in "abcdefghijklmnopqrstuvwxyz"}
        
        def find(x):
            if parent_dict[x] != x:
                parent_dict[x] = find(parent_dict[x])
            return parent_dict[x]

        for c1, c2, c3, c4 in equations:
            if c2 == c3:
                p_c1, p_c4 = find(c1), find(c4)
                parent_dict[p_c1] = p_c4

        for c1, c2, c3, c4 in equations:
            p_c1, p_c4 = find(c1), find(c4)
            if c2 != c3 and p_c1 == p_c4:
                    return False

        return True
