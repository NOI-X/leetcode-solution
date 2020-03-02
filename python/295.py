#!/usr/bin/env python
# coding=utf-8

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        # left_size >= right_size
        self.minheap = []  # right
        self.maxheap = []  # left


    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        if len(self.maxheap) > 0 and num > -1 * self.maxheap[0]:
            heapq.heappush(self.minheap, num)
        else:
            heapq.heappush(self.maxheap, -1 * num)

        if len(self.maxheap) - len(self.minheap) >= 2:
            val = -1 * heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)
        elif len(self.maxheap) - len(self.minheap) < 0:
            val = heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, -1 * val)

        # print(self.minheap, self.maxheap)


    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.maxheap) == 0:
            return None
        if len(self.maxheap) - len(self.minheap) == 1:
            return -1 * self.maxheap[0]
        else:
            return (-1 * self.maxheap[0] + self.minheap[0]) / 2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
