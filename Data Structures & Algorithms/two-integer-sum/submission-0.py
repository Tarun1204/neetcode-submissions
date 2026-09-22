class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i , value in enumerate(nums):
            a = target - value

            if a in s:
                return ([s[a],i])
            s[value] = i