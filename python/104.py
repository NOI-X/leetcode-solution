#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.DFS(root)

    def DFS(self, root):
        if root is None:
            return 0
        left = self.DFS(root.left)
        right = self.DFS(root.right)
        return max(left, right) + 1
