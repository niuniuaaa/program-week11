# #week11

## ##leetcode106、107、108、109、活动安排问题、数字拼接问题

### ###leetcode106

首先，如果数组大小为零的话，说明是空结点；如果不为空，取后序数组最后一个元素作为节点元素

其次，找到后序数组最后一个元素在中序数组的位置，作为切割点；将中序数组分割成中序左数组和中序右数组；用同样的方法切割后续数组

最后，递归处理左区间和右区间

### ###leetcode107

首先，创建队列，将根节点root放入队列，然后取出队列中的第一个元素暂存在数组中，如果孩子不为空，也放入队列中

其次，第一遍遍历完，队列中为root的两个孩子，第二次循环先遍历左孩子的左右孩子，再遍历右孩子的左右节点

最后，循环往复就可以从上到下、从左到右遍历完

### ###leetcode108

因为二叉搜索树的中序遍历结果为递增序列，思路就很明确了

1.函数输入的数组为递增数组，选取中点为根节点，构造该节点的左子树与右子树

2.当输入的递增数组为空，只能构成空树，返回空节点，调用结束

3.当构造每个节点的左右子树时，对递增数组进行拆分并进行递归调用

### ###leetcode109

首先，借用链表框架构造一个链表

其次，主要功能函数为sortedlisttobst，通过调用递归函数chainstree函数实现

chain2tree：同数组的分治法思路相同，此处不再赘述

### ###活动安排问题

首先，对活动的二维数组按照第二项x[1]的大小即活动结束时间排序

其次，第一个肯定入选，之后的判断条件为：当活动开始时间大于等于最后一个入选活动的结束时间，则不冲突，可以入选

### ###数字拼接问题

首先，首字数大的排在最前排序问题由my_cmp实现

其次，sort对列表进行排序

最后，调用"".join(li)#在li各个元素之间，用“”连接







###                   

