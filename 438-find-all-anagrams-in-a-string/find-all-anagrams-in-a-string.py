class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p)>len(s):
            return []
        seen = {}
        for ch in p:
            seen[ch] = seen.get(ch,0)+1
        window = {}
        left = 0
        result = []
        k = len(p)
        for right in range(len(s)):
            window[s[right]] = window.get(s[right],0)+1
            if right-left+1==k:
                if window==seen:
                    result.append(left)
                outgoing = s[left]
                window[outgoing]-=1
                if window[outgoing]==0:
                    del window[outgoing]
                left+=1
        return result


             






        