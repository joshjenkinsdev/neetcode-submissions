class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        num_heap = []
        for n in count.keys():
            heapq.heappush(num_heap, [count[n], n])
            if len(num_heap) > k:
                heapq.heappop(num_heap)
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(num_heap)[1])
        return ans