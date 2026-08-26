class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            largest = heapq.heappop(stones)
            next_largest = heapq.heappop(stones)
            if next_largest != largest:
                heapq.heappush(stones, largest - next_largest)
        return abs(stones[0]) if len(stones) > 0 else 0