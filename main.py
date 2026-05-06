class Queue:
    def __init__(self):
        self.q = []

    def push(self, msg):
        self.q.append(msg)

    def pop(self):
        if self.q:
            return self.q.pop(0)

queue = Queue()

queue.push("Send email")
queue.push("Process payment")

print(queue.pop())
print(queue.pop())
