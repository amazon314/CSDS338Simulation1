import time


class PriorityQueue:

    # queue = []

    def __init__(self, arr):
        self.queue = arr

    def removeProcess(self, process1):
        self.queue.remove(process1)
        self.runProcess(process1)

    def runProcess(self, process2):
        process2.setStatus("In Progress")
        print("Process " + str(process2.getPID()) + process2.getJobStatus())

        time.sleep(process2.getTime())
        process2.setStatus("Finished")
        print(process2.getPID() + " is status " + process2.getJobStatus())
        self.findHighestPriority()

    def insertProcess(self, process0):
        self.queue.append(process0)

    def findHighestPriority(self):
        arr = []
        for b in self.queue:
            arr.append(b.getPID())
        print(str(arr))
        hp = 2
        for i in self.queue:
            if i.getPriority() < hp:
                hp = i.getPriority()
        for j in self.queue:
            if j.getPriority() == hp:
                # self.queue.remove(j)
                self.removeProcess(j)
                # runProcess(j)
                break
            '''
            else:
                print("else")
            '''


class Process:
    '''
    processID = ""
    jobPriority = 0
    timeSlice = 0
    '''
    jobStatus = "pending"

    def __init__(self, PID, priority, times):
        self.processID = PID

        self.jobPriority = priority
        self.timeSlice = times

    def getPID(self):
        return self.processID

    def getPriority(self):
        return self.jobPriority

    def getTime(self):
        return self.timeSlice

    def getJobStatus(self):
        return self.jobStatus


    def setPriority(self, pri):
        self.jobPriority = pri

    def setTimeSlice(self, ts):
        self.timeSlice = ts

    def setStatus(self, js):
        self.jobStatus = js


proc1 = Process("proc1", 1, 5)
proc2 = Process("proc2", 0, 3)
proc3 = Process("proc3", 1, 10)
proc4 = Process("proc4", 0, 8)
q = PriorityQueue([proc1, proc2, proc3, proc4])
q.findHighestPriority()

