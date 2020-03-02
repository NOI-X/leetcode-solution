#!/usr/bin/env python
# coding=utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """

        hashmap = {}
        cur = head
        dummy = Node(-1)
        tail = dummy
        # copy linked list first
        while cur is not None:
            newNode = Node(cur.val)
            tail.next = newNode
            tail = tail.next
            hashmap[cur] = newNode
            cur = cur.next
        cur = head
        tail = dummy.next
        while cur is not None:
            if cur.random is not None:
                tail.random = hashmap[cur.random]
            cur = cur.next
            tail = tail.next

        return dummy.next
