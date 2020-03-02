#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if root is None:
            return False

        return self.DFS(root, sum)

    def DFS(self, root, sum):
        if root.left is None and root.right is None:
            return sum == root.val
        if root.left:
            left = self.DFS(root.left, sum - root.val)
            if left:
                return True
        if root.right:
            right = self.DFS(root.right, sum - root.val)
            return right
        return False
