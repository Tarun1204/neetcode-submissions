class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if all(num == 0 for num in nums):
            return 0
        
        p2, p1 = 0,0
        for num in nums:
            current = max(p2 + num, p1)
            p2 , p1 = p1, current
        return p1
        