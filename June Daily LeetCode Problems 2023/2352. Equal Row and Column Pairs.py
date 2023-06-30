class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        counter=collections.Counter()
        for row in grid:
            counter[tuple(row)]+=1


        ans=0
        n=len(grid)
        for i in range(n):
            now=[]
            for j in range(n):
                now.append(grid[j][i])

            ans+=counter[tuple(now)]

        return ans