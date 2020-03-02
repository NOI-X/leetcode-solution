#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for i in range(len(intervals)):
            events.append((intervals[i][0], 0))
            events.append((intervals[i][1], 1))
        events.sort()

        res = []
        L, R, cnt = -1, -1, 0
        for i in range(len(events)):
            if events[i][1] == 0:
                cnt += 1
            else:
                cnt -= 1
            if L == -1:
                L = events[i][0]
            if cnt == 0:
                res.append([L, events[i][0]])
                L = -1

        return res
