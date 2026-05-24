#https://neetcode.io/problems/is-anagram/history?submissionIndex=0

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
    
        
ex=Solution()
print(ex.isAnagram('racecar','carrace'))
