class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone_1 = len(stones) - 1
            x = stones[stone_1]
            stone_2 = len(stones) - 2
            y = stones[stone_2]

            if x > y:
                stones[stone_1] = x - y
                del stones[stone_2]
                stones.sort()
            elif y > x:
                stones[stone_2] = y - x
                del stones[stone_1]
                stones.sort()
            else:
                del stones[stone_1]
                del stones[stone_2]
        
       
        return stones[0] if stones else 0

                

            
        