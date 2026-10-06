class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_count = addition=0
        for ch in s:
            
            if ch=='(':
                open_count+=1
            elif open_count:
                open_count-=1
            else:
                addition+=1
        return addition+open_count


        
        
        

        