class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        seen = {}
        for ch in s1:
            seen[ch] = seen.get(ch,0)+1
        left = 0
        window = {}
        k = len(s1)
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right],0)+1
            if right-left+1==k:
                if window == seen:
                    return True
                outgoing = s2[left]
                window[outgoing]-=1
                if window[outgoing]==0:
                    del window[outgoing]
                left+=1
        return False


        