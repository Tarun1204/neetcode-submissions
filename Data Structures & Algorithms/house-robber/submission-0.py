class Solution:
    def rob(self, nums: List[int]) -> int:
        p2, p1 = 0,0
        for num in nums:
            current = max(p2 + num, p1)
            p2 , p1 = p1, current
        return p1
        