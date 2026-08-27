class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        minHeap = []
        for key in counts.keys():
            heapq.heappush(minHeap, [counts[key], key])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])
            
        return ans