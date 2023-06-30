import collections


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:

        i2diff2list = dict()
        ln = len(nums)

        for i in range(ln):
            for nxt in range(ln - 1, i, -1):
                if i not in i2diff2list:
                    i2diff2list[i] = dict()
                diff = nums[nxt] - nums[i]
                i2diff2list[i][diff] = nxt

        @lru_cache(None)
        def dp(i, diff):  # return int, longest sequence with this diff
            res = 0
            if i in i2diff2list and diff in i2diff2list[i]:
                nxt = i2diff2list[i][diff]
                res = max(res, dp(nxt, diff))
            return res + 1

        ans = 0
        for i in range(ln):
            for nxt in range(i + 1, ln):
                diff = nums[nxt] - nums[i]
                ans = max(ans, dp(nxt, diff) + 1)
        return ans