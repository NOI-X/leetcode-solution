#!/usr/bin/env python
# coding=utf-8
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        cntL, cntR = 0, 0
        for i in s:
            if i == '(':
                cntL += 1
            elif i == ')':
                if cntL == 0:
                    cntR += 1
                else:
                    cntL -= 1
                
        self.DFS(s, 0, res, cntL, cntR)
        return res
    
    def DFS(self, s, start, res, cntL, cntR):
        
        if cntL == 0 and cntR == 0 and self.isValid(s):
            res.append(s[:])
            return
        
        for i in range(start, len(s)):
            if i > start and s[i] == s[i - 1]:
                continue
            if s[i] == '(' and cntL > 0:
                self.DFS(s[:i] + s[i+1:], i, res, cntL - 1, cntR)
            if s[i] == ')' and cntR > 0:
                self.DFS(s[:i] + s[i+1:], i, res, cntL, cntR - 1)
            
    
    
    def isValid(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            if cnt < 0:
                return False
        return cnt == 0
        
