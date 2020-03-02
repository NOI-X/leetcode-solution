#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """

        size, res = self.DFS(root, k)
        return res.val

    def DFS(self, root, k):
        if root is None:
            return (0, None)
        left, res = self.DFS(root.left, k)
        if res:
            return (0, res)
        if left == k - 1:
            return (0, root)
        right, res = self.DFS(root.right, k - left - 1)
        return (left + 1 + right, res)
