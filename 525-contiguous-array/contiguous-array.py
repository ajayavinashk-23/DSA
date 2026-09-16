class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        balance = 0
        count = {0:-1}
        ans = 0
        for i,num in enumerate(nums):
            if num==0:
                balance -=1
            else:
                balance+=1
            if balance in count:
                ans = max(ans,i-count[balance])
            else:
                count[balance]=i
        return ans


        