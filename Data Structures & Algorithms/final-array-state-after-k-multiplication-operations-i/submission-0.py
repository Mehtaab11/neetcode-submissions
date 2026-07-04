class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        while k > 0:
            minElem = min(nums)

            index = nums.index(minElem)

            nums[index]  = multiplier * minElem

            k -=1
        
        return nums