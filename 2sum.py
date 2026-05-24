class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in hash_map:
                return [hash_map[diff], i]

            hash_map[num] = i
            
        return []

        
ex=Solution()
print(ex.twoSum([1,2,3,4],7))
