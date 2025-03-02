import random

from Queue import Queue


class Printer:
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is None:
            return False
        else:
            return True

    def startNext(self, network):
        self.currentTask = network
        self.timeRemaining = network.getPages() * 60 / self.pageRate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagePerMinte):
    labprinter = Printer(pagePerMinte)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if not labprinter.busy() and not printQueue.isEmpty():
            nextTask = printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond))
            labprinter.startNext(nextTask)

        labprinter.tick()

    averageWait = sum(waitingtimes) / len(waitingtimes)

    print(f"平均等待时间：{averageWait:6.2F}s，还有{printQueue.size()} 个任务未打印")


for i in range(10):
    simulation(3600, 10)
