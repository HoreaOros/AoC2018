from collections import deque
class Worker:
    def __init_(self, value):
        self.Value = value
        self.Job = None
    def Tick(self):
        if self.Value > 0:
            self.Value -= 1
            if self.Value == 0:
                self.Idle = True
        
    def Idle(self):
        return self.Value == 0
    def AssignJob(self, job):
        self.Idle = False
        self.Job = job
        self.Value = 60 + ord(job) - ord('A') + 1

class Scheduler:
    def __init_(self, count):
        self.Time = 0
        self.Count = count
        self.Queue = deque()
        self.Workers = []
        for _ in range(count):
            self.Workers.append(Worker(0))

    def Tick(self):
        self.Time += 1
        for w in self.Workers:
            if not w.Idle():
                w.Tick()
    
    
        
    def AddJob(self, job):
        self.Queue.append(job)

    def ClearJobs(self):
        self.Queue.clear()

    def Schedule(self):
        for w in self.Workers:
            if w.Idle():
                if len(self.Queue) > 0:
                    w.AssignJob(self.Queue.popleft())
                else:
                    break