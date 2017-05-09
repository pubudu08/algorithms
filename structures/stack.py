class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        """
        put the given item to the top of the stack, very simple operation, can be done in O(1)
        """
        self.stack.append(data)

    def pop(self):
        """
        We take the last item we have inserted to the top of the stack LIFO
        Complexity is O(1)
        """
        data = self.stack[-1]  # last element of the array
        del self.stack[-1]  # remove the last item
        return data

    def peek(self):
        return self.stack[-1]

    def sizeStack(self):
        return len(self.stack)


stack = Stack()
stack.push(12)
stack.push(34)
stack.push(6)
stack.push(23)
print(str(stack))
print("Size: " + str(stack.sizeStack()))
print("Popped: " + str(stack.pop()))
print("Popped: " + str(stack.pop()))
print("Popped: " + str(stack.pop()))
print("Size: " + str(stack.sizeStack()))
print("Peek: " + str(stack.peek()))
