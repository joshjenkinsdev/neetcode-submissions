class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            if numbers[left] + numbers[right] == target:
                break
            if right == left + 1:
                left += 1
                right = len(numbers) - 1
            else:
                right -= 1
        return [left+1, right+1]