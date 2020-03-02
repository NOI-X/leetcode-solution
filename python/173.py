#!/usr/bin/env python
# coding=utf-8

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root != None:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        ans = self.stack[-1]
        if self.stack[-1].right != None:
            root = self.stack[-1].right
            while root != None:
                self.stack.append(root)
                root = root.left
        else:
            cur = self.stack[-1]
            self.stack.pop()
            while len(self.stack) > 0 and cur is self.stack[-1].right:
                cur = self.stack[-1]
                self.stack.pop()
        return ans.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0



# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
