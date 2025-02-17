import java.util.Stack;

class MinStack {
    private Stack<Integer> stack;
    private Stack<Integer> minStack;
    private int capacity;

    public MinStack(int capacity) {
        this.capacity = capacity;
        stack = new Stack<>();
        minStack = new Stack<>();
    }

    // Check if the stack is full (overflow)
    public boolean isFull() {
        return stack.size() == capacity;
    }

    // Check if the stack is empty (underflow)
    public boolean isEmpty() {
        return stack.isEmpty();
    }

    // Push element onto stack
    public void push(int value) {
        if (isFull()) {
            System.out.println("Overflow: Stack is full");
            return;
        }
        stack.push(value);
        if (minStack.isEmpty() || value <= minStack.peek()) {
            minStack.push(value);
        }
        System.out.println("Pushed: " + value);
    }

    // Pop element from stack
    public void pop() {
        if (isEmpty()) {
            System.out.println("Underflow: Stack is empty");
            return;
        }
        int removedValue = stack.pop();
        if (removedValue == minStack.peek()) {
            minStack.pop();
        }
        System.out.println("Popped: " + removedValue);
    }

    // Get the top element of the stack
    public int top() {
        if (isEmpty()) {
            System.out.println("Stack is empty");
            return -1; // Return -1 if stack is empty
        }
        return stack.peek();
    }

    // Get the minimum element in the stack
    public int getMin() {
        if (minStack.isEmpty()) {
            System.out.println("Stack is empty");
            return -1; // Return -1 if stack is empty
        }
        return minStack.peek();
    }

    // Display the stack elements
    public void display() {
        System.out.println("Stack elements: " + stack);
    }

    public static void main(String[] args) {
        MinStack minStack = new MinStack(5); // Create a stack with capacity of 5

        minStack.push(3);
        minStack.push(5);
        minStack.push(2);
        minStack.push(1);
        minStack.push(4);
        minStack.push(6); // Should show overflow message

        minStack.display();

        System.out.println("Top element: " + minStack.top());
        System.out.println("Minimum element: " + minStack.getMin());

        minStack.pop();
        minStack.pop();
        minStack.display();

        System.out.println("Top element: " + minStack.top());
        System.out.println("Minimum element: " + minStack.getMin());
    }
}
