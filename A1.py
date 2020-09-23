import time


class PriorityQueue:

    # queue = []

    def __init__(self, arr):
        self.queue = arr
        self.burstTimes0 = []
        self.burstTimes1 = []
        self.responseTimes0 = []
        self.responseTimes1 = []
        self.timeInProcess = 0
        self.responseTime = 0

    def addBurst0(self, currentBurst):
        self.burstTimes0.append(currentBurst)

    def addBurst1(self, currentBurst):
        self.burstTimes1.append(currentBurst)

    def listBurst(self, tmpArray):
        avgResponse = 0.0
        for i in tmpArray:
            avgResponse+=i
        if len(tmpArray) > 0:
            avgResponse = avgResponse/(len(tmpArray))
        return str(avgResponse)

    def addResponse0(self, currentResponse):
        self.responseTimes0.append(currentResponse)

    def addResponse1(self, currentResponse):
        self.responseTimes1.append(currentResponse)

    def listResponse(self, tmpArray):
        avgResponse = 0.0
        for i in tmpArray:
            avgResponse+=i
        if len(tmpArray) > 0:
            avgResponse = avgResponse/(len(tmpArray))
        return str(avgResponse)

    def removeProcess(self, process1):
        self.queue.remove(process1)
        self.runProcess(process1)

    def runProcess(self, process2):
        timerStart = time.perf_counter()
        process2.setStatus("In Progress")
        print("Process " + str(process2.getPID()) + process2.getJobStatus())
        time.sleep(process2.getTime())
        process2.setStatus("Finished")
        timerEnd = time.perf_counter()
        print(process2.getPID() + " is status " + process2.getJobStatus())
        timeTaken = timerEnd-timerStart
        self.responseTime += timerEnd
        self.timeInProcess += timeTaken
        
        if process2.getPriority() == 0:
            self.addBurst0(timeTaken)
            self.addResponse0(timerEnd)
        else:
            self.addBurst1(timeTaken)
            self.addResponse1(timerEnd)
        print("Timeslice for " + str(process2.getPID()) + ": " + str(timeTaken))
        print("Average Burst Completion Time Priority 0: " + str(self.listBurst(self.burstTimes0)))
        print("Average Burst Completion Time Priority 1: " + str(self.listBurst(self.burstTimes1)))
        print("Average Response Time Priority 0: " + str(self.listResponse(self.responseTimes0)))
        print("Average Response Time Priority 1: " + str(self.listResponse(self.responseTimes1)))
        print("Context Switching Time: " + str(timerEnd-self.timeInProcess))
        contextSwitching = timerEnd-self.timeInProcess
        percentCS = (contextSwitching/timerEnd)*100
        print("Percent of Time Context Switching: " + str(percentCS))
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

