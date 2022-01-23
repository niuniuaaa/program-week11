class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution():
    def buildTree(self, inorder, postorder):
        if len(inorder) == 0:
            return None  # 树为空
        if len(inorder) == 1:
            return TreeNode(inorder[0])  # 返回唯一一个节点
        i = inorder.index(postorder[-1])#在中序遍历中找到根节点的索引
        N = TreeNode(postorder[-1])#根节点为后序遍历的最后一个节点
        N.left = self.buildTree(inorder[:i], postorder[:i])
        #分治法划分左右子树，返回根节点，这里是返回根节点，而不是数值
        N.right = self.buildTree(inorder[i + 1:], postorder[i:-1])
        return N


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]
a = Solution()
print(a.buildTree(inorder, postorder).val)
