class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_product  = float('-inf')
        product = 1
        
        for n in nums:
            product = product * n
            max_product = max(product,max_product)
            if product == 0:
                product = 1
        product = 1
        
        for index in range(len(nums) -1, -1,-1):
            product = product * nums[index]
            max_product = max(product, max_product)
            if product == 0:
                product = 1

        return max_product
        
        
