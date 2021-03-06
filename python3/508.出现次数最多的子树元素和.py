#
# @lc app=leetcode.cn id=508 lang=python3
#
# [508] 出现次数最多的子树元素和
#
# https://leetcode-cn.com/problems/most-frequent-subtree-sum/description/
#
# algorithms
# Medium (56.32%)
# Total Accepted:    1.1K
# Total Submissions: 1.9K
# Testcase Example:  '[5,2,-3]'
#
# 
# 给出二叉树的根，找出出现次数最多的子树元素和。一个结点的子树元素和定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。然后求出出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的元素（不限顺序）。
# 
# 
# 
# 示例 1
# 输入:
# 
# ⁠ 5
# ⁠/  \
# 2   -3
# 
# 
# 返回 [2, -3, 4]，所有的值均只出现一次，以任意顺序返回所有值。
# 
# 示例 2
# 输入:
# 
# ⁠ 5
# ⁠/  \
# 2   -5
# 
# 
# 返回 [2]，只有 2 出现两次，-5 只出现 1 次。
# 
# 
# 
# 提示： 假设任意子树元素和均可以用 32 位有符号整数表示。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self, node):
            l = self.dfs(node.left) if node.left else 0
            r = self.dfs(node.right) if node.right else 0
            s = node.val + l + r
            self.d[s] = self.d.get(s, 0) + 1
            return s
    
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.d = {}
        
        if not root:
            return []
        self.dfs(root)
        maxv = max(self.d.values())
        res = list(filter(lambda x : self.d[x] == maxv, self.d))
        return res
        

