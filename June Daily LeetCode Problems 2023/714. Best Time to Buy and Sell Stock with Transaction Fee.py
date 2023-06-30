class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        bsp = -prices[0]
        ssp = 0

        for i in range(1, len(prices)):
            nbsp = max(bsp, ssp - prices[i])
            nssp = max(ssp, prices[i] + bsp - fee)

            bsp = nbsp
            ssp = nssp

        return ssp
