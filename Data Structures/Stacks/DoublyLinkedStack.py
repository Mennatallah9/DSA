class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedStack:
    def __init__(self, head=None, tail=None, size=0):
        self.head = head
        self.size = size

    def stackPush(self, element):
        newNode = Node(element)
        if self.isEmpty():
            self.head = newNode
        else:
            self.head.prev = newNode
            self.head.prev.next = self.head
            self.head = self.head.prev
        self.size+=1

    def stackPop(self):
        if self.isEmpty():
            raise "Error: Stack is empty"
        popped = self.head.val
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        self.size-=1
        return popped
    
    def isEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            raise "Error: Stack is empty"
        return self.head.val
    
if __name__ == '__main__':
    # Test:
    stack = DoublyLinkedStack()
    stack.stackPush(2)
    stack.stackPush(3)
    stack.stackPush(4)
    stack.stackPush(5)
    print(stack.stackPop())
    print(stack.isEmpty())
    print(stack.peek())
    print(stack.length())