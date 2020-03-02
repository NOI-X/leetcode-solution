#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow:
                break
            fast = fast.next.next
            slow = slow.next

        if fast is None or fast.next is None:
            return None
        slow = head
        fast = fast.next
        while fast is not slow:
            fast = fast.next
            slow = slow.next

        return fast

