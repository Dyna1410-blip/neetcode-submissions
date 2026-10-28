class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        count_sort = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))    
        topk = list(count_sort)[:k]
        return topk