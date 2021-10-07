# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root):


        res = self.dfs(root)
        if res == -1:
            return False
        else:
            return True


    def dfs(self, root):



        if root == None:
            return 0

        left = self.dfs(root.left)

        right = self.dfs(root.right)

        if abs(left - right) >= 2 or left == -1 or right == -1:

            return - 1

        else:

            return max(left, right) + 1