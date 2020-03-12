import time, math

start_time = time.time()

# Use subclasses!!


class Storage:
    def __init__(self):
        self.stack = []

    @property
    def __str__(self):
        return str(self.stack)

    def add(self, n):
        self.stack =

    def retrieve(self, n):
        if self.stack[n]:
            self.stack.pop(0)
            return self.stack[0]

a = Storage()
a.add(5)
a.add(15)
a.add(25)
print a
a.retrieve(1)
print a
print 'time taken is', time.time() - start_time, 'seconds'