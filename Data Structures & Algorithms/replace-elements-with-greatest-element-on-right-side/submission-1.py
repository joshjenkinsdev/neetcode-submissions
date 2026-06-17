class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_num = -1
        new_arr = [-1]*len(arr)
        for i in range(len(arr)):
            if i == len(arr):
                break
            for j in range(i + 1, len(arr)):
                new_arr[i] = max(new_arr[i], arr[j])
        return new_arr
                
        