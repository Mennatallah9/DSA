# Implementing a Stack Using a Fixed Array

class ArrayStack:
    def __init__(self, data=[], maxSize=float("inf")):
        self.data = data
        self.maxsize = maxSize
    
    def stackPush(self, element):
        if self.isFull():
            raise "Error: Stack is full"
        self.data.append(element)

    def stackPop(self):
        if self.isEmpty():
            raise "Error: Stack is empty"
        return self.data.pop()

    def isEmpty(self):
        return self.length() == 0   # or return self.data == []

    def isFull(self):
        return self.length() == self.maxsize 

    def length(self):
        count = 0
        for _ in self.data:
            count+=1
        return count
    
    def top(self):
        if self.isEmpty():
            raise "Error: Stack is empty"
        return self.data[-1]


if __name__ == '__main__':
    # Test:
    stack = ArrayStack()
    stack.stackPush(2)
    stack.stackPush(3)
    stack.stackPush(4)
    stack.stackPush(5)
    print(stack.stackPop())
    print(stack.isFull())
    print(stack.top())
    print(stack.length())

    