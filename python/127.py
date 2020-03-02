#!/usr/bin/env python
# coding=utf-8

import collections

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        dict = set()
        for word in wordList:
            dict.add(word)
        return self.BFS(beginWord, endWord, dict)


    def BFS(self, start, end, wordList):
        vis = set()
        vis.add(start)
        Q = collections.deque()
        Q.append((start, 1))
        while len(Q) > 0:
            cur, step = Q.popleft()
            for next in self.getNext(cur, wordList):
                if next in vis:
                    continue
                if next == end:
                    return step + 1
                vis.add(next)
                Q.append((next, step + 1))
        return 0

    def getNext(self, a, wordList):
        g = []
        for i in range(0, len(a)):
            for j in 'abcdefghijklmnopqrstuvwxyz':
                if a[i] == j:
                    continue
                t = a[0:i] + j + a[i+1:]
                if t in wordList:
                    g.append(t)
        return g

