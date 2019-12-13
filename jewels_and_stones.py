class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jewels = 0
        for jewel in S :
            if jewel in J:
                jewels += 1
        return jewels