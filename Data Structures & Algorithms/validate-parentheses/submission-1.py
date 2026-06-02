class Solution:
    '''
    We can validate the strings by storing them in a stack, we only need some rules:

    1. If the current character is an opening one, add it to the stack - (,{,[
    2. If the current character is a closing one, check the top of the stack:
        1. If the stack is emtpy, return False,
        2. If the top of the stack is another king of parentheses, return False
        3. If the top of the stack matches, pop it from the stack.
    3. Continue these checks until the string is finished.
    4. At the end check if the stack is empty, if it is return True
    '''
    def isValid(self, s: str) -> bool:
        opening = {'(', '[', '{'}
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []

        for c in s:
            if c in opening:
                stack.append(c)
            elif len(stack) == 0:
                return False
            elif stack[-1] != pairs[c]:
                return False
            else:
                stack.pop()

        return len(stack) == 0