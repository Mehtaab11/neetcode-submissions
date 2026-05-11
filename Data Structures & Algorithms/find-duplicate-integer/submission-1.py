class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] +=1
            else:
                freq[num] = 1

        ans = sorted(nums, key = lambda x :freq[x])
        return ans[-1]
        
