class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        h = []; res = []
        for i in range(min(len(nums1), k)):
            tup = [nums1[i], nums2[0]]
            heapq.heappush(h, [sum(tup), tup, 0])
        while k>0 and len(h)>0:
            v = heapq.heappop(h)
            res.append(v[1])
            ind = v[2] + 1
            if ind != len(nums2):
                tup = [v[1][0], nums2[ind]]
                heapq.heappush(h, [sum(tup), tup, ind])
            k -= 1

        return res