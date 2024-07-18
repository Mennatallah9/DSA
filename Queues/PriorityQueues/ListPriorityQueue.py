# implementation of priority queue using a list

class PriorityQueue:
    def __init__(self, queue=[]):
        self.queue = queue

    def insert(self, element):
        self.queue.append(element)
        self.queue.sort(reverse=True)

    def delete(self):
        if self.isEmpty():
            raise "Error: Queue is empty"
        deleted = self.queue[0]
        del self.queue[0]
        return deleted
    
    def isEmpty(self):
        return self.length() == 0
    
    def length(self):
        count = 0
        for _ in self.queue:
            count += 1
        return count
    
    def display(self):
        for element in self.queue:
            print(element, end=" ")

if __name__ == "__main__":        
    # Test
    q = PriorityQueue()
    q.insert(10)
    q.insert(20)
    q.delete()
    q.insert(5)
    q.insert(15)
    q.display()
    
    