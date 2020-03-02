#!/usr/bin/env python
# coding=utf-8

class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.capacity = k
        self.queue = nums
        heapq.heapify(self.queue)
        #for num in nums:
        #    self.add(num)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.queue, val)
        if len(self.queue) > self.capacity:
            heapq.heappop(self.queue)
        return self.queue[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
