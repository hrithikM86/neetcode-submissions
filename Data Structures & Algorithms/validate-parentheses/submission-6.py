from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        match = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in match.values():
                stack.append(ch)
            else:
                if not stack or stack.pop() != match.get(ch):
                    return False

        return not stack