#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next

        return False