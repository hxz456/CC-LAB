def evaluate_postfix(expression):
    stack = []

    for char in expression:
        if char.isdigit():
            stack.append(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()

            if char == '+':
                result = operand1 + operand2
            elif char == '-':
                result = operand1 - operand2
            elif char == '*':
                result = operand1 * operand2
            elif char == '/':
                result = operand1 // operand2  # Integer division

            stack.append(result)

    return stack.pop()

if __name__ == "__main__":
    expression = input("Enter Expression : ")
    expression = expression.split(" ")
    result = evaluate_postfix(expression)
    print("The result of the postfix expression is:", result)
