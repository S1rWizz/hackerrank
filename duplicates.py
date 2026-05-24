# https://neetcode.io/problems/duplicate-integer/history?list=neetcode150&submissionIndex=0

class Solution:
    
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(nums)!=len(set(nums))
        
ex=Solution()
print(ex.hasDuplicate([1,2,3,4,5]))
