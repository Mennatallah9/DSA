class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class SinglyLinkedQueue:
    def __init__(self, head=None, size=0):
        self.head = head
        self.size = size

    def queueEnqueue(self, element):
        newNode = Node(val=element)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1

    def queueDequeue(self):
        if self.isEmpty():
            raise "Error: Queue is empty"
        curr = self.head
        while curr.next.next:
            curr = curr.next
        curr.next = None
        self.size -= 1

    def isEmpty(self):
        return self.size == 0
    
    def length(self):
        return self.size
    
    def peek(self):
        if self.isEmpty():
            raise "Error: Queue is empty"
        curr = self.head
        while curr.next:
            curr = curr.next
        return curr.val
    

if __name__ == '__main__':
    # Test:
    queue = SinglyLinkedQueue()
    queue.queueEnqueue(2)
    queue.queueEnqueue(3)
    queue.queueEnqueue(4)
    queue.queueEnqueue(5)
    print(queue.peek())
    queue.queueDequeue()
    print(queue.peek())
    print(queue.length())
    print(queue.isEmpty())