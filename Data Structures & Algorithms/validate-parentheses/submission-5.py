from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for letter in s:
            if letter in ('(', '[', '{'):
                stack.append(letter)
            else:
                if len(stack)>0:
                    open_br = stack.pop()
                else:
                    return False
                if open_br == '(' and letter == ')':
                    continue
                elif open_br == '[' and letter == ']':
                    continue
                elif open_br == '{' and letter == '}':
                    continue
                else:
                    return False

        return True if len(stack) == 0 else False





        