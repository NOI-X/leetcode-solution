#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        cur = dummy
        heap = []
        [heapq.heappush(heap, (l.val, l)) for i, l in enumerate(lists) if l]

        while heap:
            curVal, curHead = heapq.heappop(heap)
            curNext = curHead.next
            cur.next = curHead
            curHead.next = None
            cur = curHead
            curHead = curNext
            if curHead:
                heapq.heappush(heap, (curHead.val, curHead))
        return dummy.next




