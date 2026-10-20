class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        values_seen = set()
        
        for num in nums:
            if num in values_seen:
                return True
            values_seen.add(num)
            
        return False