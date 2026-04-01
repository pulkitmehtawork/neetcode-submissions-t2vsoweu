class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for token in tokens:
            if token in ["+", "*", "/", "-"]:
                
                operator = token#stack.pop()
                second_operand = int(stack.pop())
                first_operand = int(stack.pop())
                if operator == "+":
                    val = first_operand  + second_operand
                elif operator == "-":
                    val = first_operand  - second_operand
                elif operator == "*":
                    val = first_operand  * second_operand
                else:
                    val = float(first_operand  / second_operand)
                stack.append(val)
            else:
                stack.append(int(token))
            print(stack)
        return int(stack[-1])

        