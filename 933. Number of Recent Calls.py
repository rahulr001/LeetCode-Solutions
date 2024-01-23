from queue import deque


class RecentCounter:

    def __init__(self):
        self.counter = deque()

    def ping(self, t: int) -> int:
        self.counter.append(t)

        while self.counter[0] < (t - 3000):
            self.counter.popleft()
        return len(self.counter)


obj = RecentCounter()
param_1 = obj.ping(1)
param_1 = obj.ping(100)
param_1 = obj.ping(3001)
param_1 = obj.ping(3002)

print(param_1)
