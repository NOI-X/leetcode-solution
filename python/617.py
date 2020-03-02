#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        return self.DFS(t1, t2)

    def DFS(self, root1, root2) :

        if root1 is None and root2 is None:
            return None
        if root1 is None and root2 is not None:
            return root2
        if root1 is not None and root2 is None:
            return root1

        root1.left = self.DFS(root1.left, root2.left)
        root1.right = self.DFS(root1.right, root2.right)
        root1.val = root1.val + root2.val
        return root1


