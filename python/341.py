#!/usr/bin/env python
# coding=utf-8

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []
        for e in nestedList[::-1]:
            self.stack.append(e)

    def next(self):
        """
        :rtype: int
        """
        return self.stack.pop()


    def hasNext(self):
        """
        :rtype: bool
        """
        # handle top to Integer
        while self.stack and not self.stack[-1].isInteger():
            top = self.stack.pop().getList()
            for e in top[::-1]:
                self.stack.append(e)


        if self.stack and self.stack[-1].isInteger():
            return True
        return False



# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
