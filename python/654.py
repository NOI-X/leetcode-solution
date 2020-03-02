#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []

        for i in range(len(nums)):
            cur = TreeNode(nums[i])
            while len(stack) > 0 and stack[-1].val < nums[i]:
                stack[-1].right = cur.left
                cur.left = stack[-1]
                stack.pop()
            stack.append(cur)

        root = stack[0]
        cur = root
        for i in range(1, len(stack)):
            cur.right = stack[i]
            cur = stack[i]

        return root


