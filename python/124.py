#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        val, start = self.DFS(root)

        return val

    def DFS(self, root):
        if root is None:
            return (0, 0)
        left, leftStart = self.DFS(root.left)
        right, rightStart = self.DFS(root.right)

        start = root.val
        start = max(start, leftStart + root.val)
        start = max(start, rightStart + root.val)
        val = max(start, leftStart + rightStart + root.val)
        if root.left:
            val = max(val, left)
        if root.right:
            val = max(val, right)

        return (val, start)

