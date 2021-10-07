# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root):

        # 需要记录是奇数层还是偶数层

        if root == None:
            return []

        queue = [root]
        count_cen = 0

        res = []

        while len(queue) != 0:

            size = len(queue)
            temp = []

            for _ in range(size):

                node = queue.pop(0)

                temp.append(node.val)
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            if count_cen % 2 == 0:

                res.append(temp)

            else:
                res.append(temp[::-1])

            count_cen += 1
        return res




