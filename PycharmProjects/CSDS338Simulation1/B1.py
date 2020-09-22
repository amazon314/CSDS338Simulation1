import time


class PriorityQueue:

    # queue = []

    def __init__(self, arr):
        self.queue = arr

    def removeProcess(self, process1):
        self.queue.remove(process1)

    def runProcess(self, process2):

        arr = []
        for i in self.queue:
            arr.append(i.getPID())

        print("queue is " + str(arr))

        if len(self.queue) > 1:

            self.removeProcess(process2)

            plevel = process2.getPriority()
            process2.setStatus("In Progress")
            print("Process " + str(process2.getPID()) + " " + process2.getJobStatus())

            if process2.getPID() == 'proc1':
                self.insertProcess(Process('proc5', 0, 10))

            hpj = None
            hp = 2
            # tf = False

            for i in self.queue:
                if i.getPriority() < hp:
                    hp = i.getPriority()
            for j in self.queue:
                if j.getPriority() == hp:
                    # tf = True
                    hpj = j
                    break

            p3 = hpj
            plevelNext = p3.getPriority()
            arr = []
            for i in self.queue:
                arr.append(i.getPID())

            print("queue is " + str(arr))
            '''
            if p3 != None:
                plevelNext = p3.getPriority()
            else:
                plevelNext = 5
            '''



            print("plevel is " + str(plevel) + " plevelnext is " + str(plevelNext))
            if plevelNext < plevel:
                process2.setStatus("pending")
                print(process2.getPID() + " is status " + process2.getJobStatus())
                self.insertProcess(process2)
                # self.removeProcess(p3)
                self.runProcess(p3)
            else:

                time.sleep(process2.getTime())
                process2.setStatus("Finished")
                print(process2.getPID() + " is status " + process2.getJobStatus())
                # self.removeProcess(p3)
                self.runProcess(p3)
        else:
            print("Process " + str(process2.getPID()) + " is running")
            process2.setStatus("In Progress")
            time.sleep(process2.getTime())
            process2.setStatus("Finished")
            print(process2.getPID() + " is status " + process2.getJobStatus())

    def insertProcess(self, process0):
        self.queue.append(process0)

    def findHighestPriority(self):
        hpj = None
        hp = 2
        #tf = False

        for i in self.queue:
            if i.getPriority() < hp:
                hp = i.getPriority()
        for j in self.queue:
            if j.getPriority() == hp:
                #tf = True
                hpj = j
                break
                # self.removeProcess(j)

        if len(self.queue) > 0:
            self.runProcess(hpj)


        '''
        if tf == False:
          hp += 1
          print("else")
        '''

        return hpj


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












