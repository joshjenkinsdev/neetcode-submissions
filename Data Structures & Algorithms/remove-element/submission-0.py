class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:   
        new_nums = [e for e in nums if e != val]
        k = len(new_nums)
        nums[:k] = new_nums
        return k