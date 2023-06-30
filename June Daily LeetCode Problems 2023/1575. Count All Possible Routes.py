class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:

        @lru_cache(None)
        def fn(n, x):
            """Return all possible routes from n to finish with x fuel."""
            if x < 0: return 0  # not going anywhere without fuel
            ans = 0
            if n == finish: ans += 1
            for nn in range(len(locations)):
                if nn != n: ans += fn(nn, x - abs(locations[n] - locations[nn]))
            return ans

        return fn(start, fuel) % 1_000_000_007ans = []