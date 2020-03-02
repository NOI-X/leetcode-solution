#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        path = []
        self.DFS(root, path)
        for i in range(len(path)):
            if i == 0:
                continue
            if path[i] <= path[i - 1]:
                return False
        return True

    def DFS(self, root, path):
        if root is None:
            return
        self.DFS(root.left, path)
        path.append(root.val)
        self.DFS(root.right, path)



'''
Solution 2
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        return self.DFS(root, float('-inf'), float('inf'))

    def DFS(self, root, minVal, maxVal):


        if root.val <= minVal:
            return False
        if root.val >= maxVal:
            return False

        left, right = True, True

        if root.left:
            self.DFS(root.left, minVal, root.val)

        if root.right:
            self.DFS(root.right, root.val, maxVal)

        return left and right

