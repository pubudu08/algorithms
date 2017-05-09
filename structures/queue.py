
class Queue(object):
    """
    FIFO
    Applications
        CPU scheduling: When the resource shared with several consumers, we store then in a queue
        IO buffers: When data is transferred asynchronously between two processes

    BFS
    """

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.queue == []

    def enqueue(self, data):
        return self.queue.append(data)

    def sizeOfQueue(self):
        return len(self.queue)

    def dequeue(self):
        data = self.queue[0]
        del self.queue[0]
        return data

    def peek(self):
        return self.queue[0]

queue = Queue()
queue.enqueue(12)
queue.enqueue(34)
queue.enqueue(6)
queue.enqueue(23)
print("Size: " + str(queue.sizeOfQueue()))
print("Dequeue: " + str(queue.dequeue()))
print("Dequeue: " + str(queue.dequeue()))
print("Dequeue: " + str(queue.dequeue()))
print("Size: " + str(queue.sizeOfQueue()))
print("Peek: " + str(queue.peek()))
