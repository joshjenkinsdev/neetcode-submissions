class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = sorted(Counter(tasks).values())
        maxf = counts[-1]
        idle = (maxf - 1) * n
        for i in range(len(counts) - 2, -1, -1):
            idle -= min(maxf - 1, counts[i])
        return max(0, idle) + len(tasks)
