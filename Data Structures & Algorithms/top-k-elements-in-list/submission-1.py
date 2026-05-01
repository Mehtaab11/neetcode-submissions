class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        
        for num, freq in count.most_common(k):
            result.append(num)

        return result