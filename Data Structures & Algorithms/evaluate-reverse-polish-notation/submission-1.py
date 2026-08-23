class Solution:

  def evalRPN(self, tokens: list[str]) -> int:
    stack = []

    for el in tokens:
      if el == "+":
        stack.append(stack.pop() + stack.pop())
      elif el == "*":
        stack.append(stack.pop() * stack.pop())
      elif el == "-":
        b = stack.pop()
        a = stack.pop()
        stack.append(a - b)
      elif el == "/":
        b = stack.pop()
        a = stack.pop()
        stack.append(int(a / b))  # Truncates toward zero
      else:
        stack.append(int(el))

    return stack[0]

        