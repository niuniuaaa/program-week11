# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
        self.head=0


    def append(self, item):
        # q为待添加的结点
        q = ListNode(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        length = len_of_chain(head)
        return chain2tree(head, length)


def chain2tree(start, limit):
    if limit <= 0: return None
    left_len = limit / 2
    right_len = limit - left_len - 1
    left = chain2tree(start, left_len)
    while left_len:
        start = start.next
        left_len -= 1
    root = TreeNode(start.val)
    root.left = left
    root.right = chain2tree(start.next, right_len)
    return root


def len_of_chain(head):
    if not head: return 0
    return len_of_chain(head.next) + 1


root = ListNode(-10)
root.append(-3)
root.append(1)
root.append(5)
root.append(9)
a = Solution()
print(a.sortedListToBST(root).val)
