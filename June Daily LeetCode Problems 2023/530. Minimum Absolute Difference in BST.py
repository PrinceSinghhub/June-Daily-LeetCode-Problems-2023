# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root):
        ans = []
        stack = []
        currNode = root

        while True:
            if currNode != None:
                stack.append(currNode)
                currNode = currNode.left

            else:
                if len(stack) == 0:
                    break
                node = stack.pop()
                ans.append(node.val)
                currNode = node.right
        return ans

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        arr = self.dfs(root)

        diff = float('inf')
        for i in range(1, len(arr)):
            diff = min(diff, abs(arr[i] - arr[i - 1]))
        return diff
