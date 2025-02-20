class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = Queue()  # This will store the final postfix expression
    operators = []  # This will be used as a stack for operators and parentheses

    for char in expression:
        if char.isalnum():  # Operand (numbers or variables)
            output.enqueue(char)
        elif char == '(':  # Left Parenthesis
            operators.append(char)
        elif char == ')':  # Right Parenthesis
            while operators and operators[-1] != '(':
                output.enqueue(operators.pop())
            operators.pop()  # Pop the '(' from the stack
        else:  # Operator (+, -, *, /, ^)
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[char]):
                output.enqueue(operators.pop())
            operators.append(char)

    # Pop all remaining operators from the stack
    while operators:
        output.enqueue(operators.pop())

    # Build the final postfix expression from the queue
    postfix_expression = ""
    while not output.is_empty():
        postfix_expression += output.dequeue()

    return postfix_expression

# Example usage
expression = "3+5*2/(1-4)^2"
postfix = infix_to_postfix(expression)
print(f"Postfix notation: {postfix}")
