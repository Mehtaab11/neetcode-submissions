class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums) 

        low = 0 
        high = n - 1

        while low < high:
            mid = low + (high - low) // 2
            elem = nums[mid]

            if elem > nums[high]:
                low = mid + 1
            else:
                high = mid
        
        pivot = low

        low = 0 
        high = pivot -1 

    
        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1

        low = pivot
        high = n - 1

        while low <= high:
            mid = low + (high - low) // 2
            
            if nums[mid] == target:
                return mid
            
            elif nums[mid] < target:
                low = mid + 1
            
            else:
                high = mid - 1
        
        return -1
        

