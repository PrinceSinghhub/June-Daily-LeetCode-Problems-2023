class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        n = row * col
        root, left, right = list(range(n)), [0] * n, [0] * n
        for i in range(col):
            for j in range(row):
                left[i * row + j] = i
                right[i * row + j] = i

        def find(x):
            if x != root[x]:
                root[x] = find(root[x])
            return root[x]

        def union(x, y):
            a, b = find(x), find(y)
            if a != b:
                root[a] = b
            left[b] = min(left[b], left[a])
            right[b] = max(right[b], right[a])

        seen = set()
        dirs = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1))
        for i, cell in enumerate(cells):
            cx, cy = cell[0] - 1, cell[1] - 1
            for dx, dy in dirs:
                x, y = cx + dx, cy + dy
                if 0 <= x < row and 0 <= y < col and (x, y) in seen:
                    union(cy * row + cx, y * row + x)
                    new = find(y * row + x)
                    if left[new] == 0 and right[new] == col - 1:
                        return i
            seen.add((cx, cy))
        return n