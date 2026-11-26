class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = {x for x in nums}
        
        if len(nums) == len(unique):
            return False
        
        return True


        
        