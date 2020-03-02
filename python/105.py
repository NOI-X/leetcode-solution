#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        return self.DFS(preorder, inorder)

    def DFS(self, preorder, inorder):
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        left_size = inorder.index(preorder[0])
        left_in_order = inorder[:left_size]
        left_pre_order = preorder[1: left_size + 1]
        # print(left_in_order, left_pre_order)
        right_in_order = inorder[left_size+1 :]
        right_pre_order = preorder[left_size+1:]
        root.left = self.DFS(left_pre_order, left_in_order)
        root.right = self.DFS(right_pre_order, right_in_order)

        return root

