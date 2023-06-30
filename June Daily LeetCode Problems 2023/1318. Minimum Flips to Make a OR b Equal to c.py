class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        return (c:=(a|b)^c).bit_count()+(a&b&c).bit_count()+1