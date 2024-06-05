class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        s_j = set(jewels)
        for i in s_j:
            res += stones.count(i)
        return res
        