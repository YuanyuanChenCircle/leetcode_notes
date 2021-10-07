class Solution:
    def verifyPostorder(self, postorder):

        return self.find(postorder)




    def find(self, postorder):

        # 递归终止条件
        if len(postorder) == 0:
            return True



        # 首先找到根节点
        root = postorder[-1]

        # 然后找到左右子树的分界点
        for i in range(len(postorder)):

            if postorder[i] > root:
                break


        # 找到右子树，进行遍历，如果出现小于根节点的，则返回false
        for j in range(i, len(postorder) - 1):

            if postorder[j] < root:
                return False




        self.find(postorder[:i]) and self.find(postorder[i:-1])



