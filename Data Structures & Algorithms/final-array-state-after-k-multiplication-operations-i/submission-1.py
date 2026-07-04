class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            minElem = min(nums)

            index = nums.index(minElem)

            nums[index]  = multiplier * minElem
        
        return nums