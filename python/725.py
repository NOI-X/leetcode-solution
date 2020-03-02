#!/usr/bin/env python
# coding=utf-8

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        ret = [None] * k  # 结果
        length, move = 0, root
        while move:
            length += 1
            move = move.next
        avg, rem = length / k, length % k
        move, indexs = root, 0  # 结果数组索引
        while move:
            tmp = move
            pre = ListNode(0)  # 当前结点的前一个结点
            pre.next = move
            num = 0
            while num < avg:  # 平均分给每个k的结点数目
                pre, move = pre.next, move.next
                num += 1
            if rem:  # 平分之后还应该分给前rem个链表每个一个结点
                pre, move = pre.next, move.next
                rem -= 1
            pre.next = None
            ret[indexs] = tmp
            indexs += 1
        return ret
