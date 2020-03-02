#!/usr/bin/env python
# coding=utf-8

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        stack = []
        slow = head
        fast = head.next
        stack.append(slow.val)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            stack.append(slow.val)
        # 偶数长度 fast.next is None
        # 奇数长度 fast is None
        if fast is None:
            stack.pop() # 奇数长度弹掉中间的那个
        slow = slow.next
        while slow:
            if stack[-1] != slow.val:
                return False
            slow = slow.next
            stack.pop()

        return True


