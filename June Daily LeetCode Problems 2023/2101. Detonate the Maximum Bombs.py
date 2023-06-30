class Solution:
    def dfs(self, src, vis, adj):
        vis[src] = 1
        for x in adj[src]:
            if vis[x] == 0:
                self.dfs(x, vis, adj)

    def maximumDetonation(self, bombs):
        n = len(bombs)
        adj = [[] for _ in range(n)]

        for i in range(n):
            r1 = bombs[i][2]
            x1 = bombs[i][0]
            y1 = bombs[i][1]

            for j in range(n):
                if i != j:
                    x2, y2, r2 = bombs[j][0], bombs[j][1], bombs[j][2]
                    dsq = (x1 - x2) ** 2 + (y1 - y2) ** 2
                    if dsq <= r1 ** 2:
                        adj[i].append(j)

        vis = [0] * n
        ans = 0

        for i in range(n):
            self.dfs(i, vis, adj)
            cnt = sum(vis)
            ans = max(ans, cnt)
            vis = [0] * n

        return ans
