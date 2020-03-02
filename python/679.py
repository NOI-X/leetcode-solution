
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        vis = [0] * 4
        return self.DFS(nums, 0, vis, [], 0)


    def DFS(self, nums, cnt, vis, s, step):

        if step == 7:
            return abs(self.cal(s) - 24) <= 1e-6

        last = -1
        for i in range(4):
            if vis[i] == 1:
                continue
            if last != -1 and nums[i] == nums[last]:
                continue
            last = i
            vis[i] = 1
            res = self.DFS(nums, cnt + 1, vis, s + [nums[i]], step + 1)
            if res:
                return True
            vis[i] = 0

        if cnt > 1:
            for i in "+-*/":
                res = self.DFS(nums, cnt - 1, vis, s + [i], step + 1)
                if res:
                    return True
        return False

    def cal(self, s):
        stack = []
        for i in s:
            if i == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif i == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif i == '/':
                a = stack.pop()
                b = stack.pop()
                if a == 0:
                    return 0
                stack.append(1.0 * b / a)
            else:
                stack.append(i)
        # print(s, stack[-1])
        return stack.pop()
