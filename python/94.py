#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root == None:
            return res
        stack = self.init(root)

        while len(stack) > 0:
            res.append(self.next(stack))
        return res

    def init(self, root):
        stack = []

        while root != None:
            stack.append(root)
            root = root.left

        return stack

    def next(self, stack):
        """
        @return the next smallest number
        :rtype: int
        """

        ans = stack[-1]
        if stack[-1].right != None:
            root = stack[-1].right
            while root != None:
                stack.append(root)
                root = root.left
        else:
            cur = stack[-1]
            stack.pop()
            while len(stack) > 0 and cur is stack[-1].right:
                cur = stack[-1]
                stack.pop()
        return ans.val


'''
Solution 2 DFS
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        if root == None:
            return res
        path = []
        self.DFS(root, path)
        return path

    def DFS(self, root, path):
        if root is None:
            return
        self.DFS(root.left, path)
        path.append(root.val)
        self.DFS(root.right, path)

