class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        n = sorted(nums)
        print(n)
        a = []
        for i in range(len(n)):

            if target == n[i]:
                a.append(i)
        return a

        