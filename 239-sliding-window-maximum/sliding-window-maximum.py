class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        result = []
        dq = deque()

        for right in range(len(nums)):

            # 1. Remove indices outside the current window
            while dq and dq[0] <= right - k:
                dq.popleft()

            # 2. Maintain decreasing order
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # 3. Insert current index
            dq.append(right)

            # 4. Record maximum once window size reaches k
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result






        