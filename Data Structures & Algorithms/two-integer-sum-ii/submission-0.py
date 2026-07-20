class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        slow, fast = 0,0
        while fast < len(numbers):
            total = numbers[slow] + numbers[fast]
            if total == target:
                return [slow + 1,fast + 1]
            if fast == len(numbers) - 1:
                slow += 1
                fast = slow + 1
            else:
                fast += 1

            
