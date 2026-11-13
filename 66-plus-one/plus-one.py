class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = ''
        for num in digits:
            s+=str(num)
        a = int(s)+1
        b = list(map(str,str(a)))
        c = []
        for e in b:
            c.append(int(e))
        return c

        

        