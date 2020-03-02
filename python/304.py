#!/usr/bin/env python
# coding=utf-8

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        if n == 0:
            m = 0
        else:
            m = len(matrix[0])

        self.presum = [[0]*(m + 1) for i in range(n + 1)]

        for i in range(n):
            for j in range(m):
                self.presum[i + 1][j + 1] = self.presum[i][j + 1] + self.presum[i + 1][j] - self.presum[i][j] + matrix[i][j]


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.presum[row2 + 1][col2 + 1] - self.presum[row2 + 1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
