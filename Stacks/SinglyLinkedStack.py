# Implementing a Stack with a Singly Linked List

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedStack:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def stackPush(self, element):
        newNode = Node(val=element)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def stackPop(self):
        if self.isEmpty():
            raise "Error: Stack is empty"
        popped = self.head
        self.head = self.head.next
        popped.next = None
        self.size -= 1
        return popped.val

    def isEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def top(self):
        if self.isEmpty():
            raise "Error: stack is empty"
        return self.head.val

    

if __name__ == '__main__':
    # Test:
    stack = SinglyLinkedStack()
    stack.stackPush(2)
    stack.stackPush(3)
    stack.stackPush(4)
    stack.stackPush(5)
    print(stack.top())
    print(stack.stackPop())
    print(stack.length())
    print(stack.isEmpty())
    