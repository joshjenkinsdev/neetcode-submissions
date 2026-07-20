class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        s1_count = {}
        window = len(s1)
        left = 0
        for right, char in enumerate(s2):

            # set s1 count while setting initial s2 count
            if right < len(s1):
                count[char] = count.get(char, 0) + 1
                s1_count[s1[right]] = s1_count.get(s1[right], 0) + 1

                # if s1_count is finished and they are both equal, then it's an instant match
                if len(s1_count) == len(s1) and count == s1_count:
                    return True
                continue
            
            # increment counter for right-most value
            count[char] = count.get(char, 0) + 1

            # if window is too big, we need to shorten it and decrement previous value (remove value if it == 0)
            if right - left >= window:
                count[s2[left]] -= 1
                if count[s2[left]] == 0:
                    del count[s2[left]]
                left += 1

            # if the count dicts are equal, we've found a permuation
            if count == s1_count:
                return True


        return False


