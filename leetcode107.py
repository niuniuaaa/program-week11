# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue=[root]#记录根节点
        res=[]#记录结果数组
        while queue:
            temp=[]#临时数组
            for _ in range(len(queue)):
                node=queue.pop(0)#首次pop root结点
                temp.append(node.val)
                #循环从上到下、从左到右记录每一层节点
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp)
        return res[::-1]


if __name__ == '__main__':
    right_tree = TreeNode(20)
    right_tree.right = TreeNode(7)
    right_tree.left = TreeNode(15)

    left_tree = TreeNode(9)

    root = TreeNode(3)
    root.right = right_tree
    root.left = left_tree
    s = Solution()
    print(s.levelOrderBottom(root))

