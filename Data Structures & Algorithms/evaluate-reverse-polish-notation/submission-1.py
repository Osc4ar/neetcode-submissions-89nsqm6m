class Solution:
    '''
    Given the format of the reverse polish notation, we can use a stack to store the operands
    and pop when an operator is found.

    1. Initialize an empty stack
    2. Iterate all the tokens
    3. If the token is not an operator, push it into the stack
    4. If the token is an operator, identify it and pop the last two values (the first one is the right operand)
        in the stack. Apply the operator and push the result into the stack.
    5. Keep repeating until all the tokens were processed.
    6. Return the top of the stack (the stack should have a single value to be valid)

    ["1","2","+","3","*","4","-"]
    
    Stack: [5]
    '''
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = []

        for t in tokens:
            if t in operators:
                right_operand = stack.pop()
                left_operand = stack.pop()
                if t == '+':
                    stack.append(left_operand + right_operand)
                elif t == '-':
                    stack.append(left_operand - right_operand)
                elif t == '*':
                    stack.append(left_operand * right_operand)
                elif right_operand == 0: # Division by zero
                    stack.append(0)
                else: # Division by non-zero values
                    stack.append(int(float(left_operand) / right_operand))
            else:
                stack.append(int(t))

        # Optionally, we could check stack size and throw an error to identify invalid expressions
        return stack[-1]