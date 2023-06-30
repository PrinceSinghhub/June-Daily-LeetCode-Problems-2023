class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        res, s, h = [-inf, -1], [root], 1
        while s:
            res = max(res, [sum(node.val for node in s), -h])
            s = [c for node in s for c in (node.left, node.right) if c]
            h += 1
        return -res[1]