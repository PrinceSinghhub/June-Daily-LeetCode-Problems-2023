from bisect import bisect_right
from cmath import inf
from functools import cache


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        @cache
        def f(i, prev):
            if i == len(arr1):
                return 0
            ans = inf
            if prev < arr1[i]:
                ans = f(i + 1, arr1[i])

            k = bisect_right(arr2, prev)
            if k < len(arr2):
                ans = min(ans, 1 + f(i + 1, arr2[k]))

            return ans

        ans = f(0, -inf)
        return ans if ans < inf else -1