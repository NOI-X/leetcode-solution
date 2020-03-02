#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        path = []
        if root == None:
            return path
        self.DFS(root, path)
        return path

    def DFS(self, root, path):
        if root is None:
            return

        self.DFS(root.left, path)
        self.DFS(root.right, path)
        path.append(root.val)

