#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#
# https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/description/
#
# algorithms
# Easy (68.85%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    44.1K
# Total Submissions: 64.1K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# 给定一个二叉树，找出其最大深度。
# 
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
# 
# 说明: 叶子节点是指没有子节点的节点。
# 
# 示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 返回它的最大深度 3 。
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        depthleft = self.maxDepth(root.left) + 1
        depthright = self.maxDepth(root.right) + 1

        return max(depthleft, depthright)

