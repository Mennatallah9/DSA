class ArrayQueue:
    def __init__(self, data=[], maxSize=float("inf")):
        self.data = data
        self.maxSize = maxSize
    
    def queueEnqueue(self, element):
        if self.isFull():
            raise "Error: Queue is full"
        self.data.append(element)

    def queueDequeue(self):
        if self.isEmpty():
            raise "Error: Queue is empty"
        return self.data.pop(0)
    
    def isEmpty(self):
        return self.data == []

    def isFull(self):
        return self.length() == self.maxSize
    
    def length(self):
        count = 0
        for _ in self.data:
            count+=1
        return count
    
    def peek(self):
        if self.isEmpty():
            raise "Error: Queue is empty"
        return self.data[0]
    
if __name__ == '__main__':
    # Test:
    queue = ArrayQueue()
    queue.queueEnqueue(2)
    queue.queueEnqueue(3)
    queue.queueEnqueue(4)
    queue.queueEnqueue(5)
    print(queue.queueDequeue())
    print(queue.isFull())
    print(queue.peek())
    print(queue.length())