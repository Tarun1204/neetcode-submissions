class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        o = {}

        for i, value in enumerate(nums):
            count = o.get(value, 0)+1
            o[value] = count
            if o[value] > 1:
                return True
                break
        else:
            return False
        