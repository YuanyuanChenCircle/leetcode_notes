# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans = 0

    def diameterOfBinaryTree(self, root):


        self.dfs(root)

        return self.ans


    def dfs(self, root):

        if root == None:
            return 0


        L = self.dfs(root.left)
        R = self.dfs(root.right)

        self.ans = max(self.ans, L + R)


        return max(L, R) + 1

