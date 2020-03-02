#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        dummy = ListNode(-1)
        left = head
        right = head.next
        cur = dummy
        while left is not None:
            delete = False
            while right is not None and left.val == right.val:
                delete = True
                right = right.next
            if not delete:
                cur.next = left
                cur = cur.next
                left = right
                if right is not None:
                    right = right.next
            else:
                if right is not None:
                    left = right
                    right = right.next
                else:
                    break

            cur.next = None

        return dummy.next


