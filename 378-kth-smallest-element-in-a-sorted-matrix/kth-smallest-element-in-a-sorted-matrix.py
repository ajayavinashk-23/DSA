class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        l = []
        for num in matrix:
            l.extend(num)
        s = sorted(l)
        if k>=len(s):
            return s[len(s)-1]
        else:
            return s[k-1]
        
            