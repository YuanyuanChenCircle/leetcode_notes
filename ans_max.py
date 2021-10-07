# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):


        if root == None:
            return None

        if root == p or root == q:
            return root

        # root！= None，不等于p，不等于q的情况下，出现的结果
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # left==None，right==None时候return None
        
        if left == None:
            return right

        if right == None:
            return left

        if left and right:
            return root

