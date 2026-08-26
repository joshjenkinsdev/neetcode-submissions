class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        maxHeap = [-c for c in counts.values()]
        heapq.heapify(maxHeap)

        task_queue = deque()
        time = 0

        while maxHeap or task_queue:
            time += 1
            if maxHeap:
                count = 1 + heapq.heappop(maxHeap)
                if count:
                    task_queue.append([count, time + n])
            if task_queue and task_queue[0][1] == time:
                heapq.heappush(maxHeap, task_queue.popleft()[0]) 

        return time