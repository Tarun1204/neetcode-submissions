class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):  
            num = nums[i]
            prev_max = max_product
            prev_min = min_product
            max_product = max(num, prev_max * num, prev_min * num)
            min_product = min(num, prev_max * num, prev_min * num)
            
            result = max(result, max_product)
        
        return result
        
