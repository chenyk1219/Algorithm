import queue


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Task:
    def __init__(self, second):
        self.currentTask = None
        # self.speed = second
        self.timeRate = second

    def tick(self):
        if self.currentTask is not None:
            self.timeRate -= 1
            if self.timeRate <= 0:
                self.currentTask = None


def solutions():
    msg = [0, 0, 0, 0, 0, 1, 1, 2, 2]
    task1 = Task(1)
    task2 = Task(2)

    queue1 = Queue()
    queue2 = Queue()

    seconds = 0
    while len(msg) <= 0:
        count = msg.count(seconds)
        if count <= 6:
            msg = msg[count:]
            for i in range(count // 2):
                queue1.enqueue(task1)
                queue2.enqueue(task2)
            if count % 2 == 1:
                queue1.enqueue(task1)
        seconds += 1


from collections import deque


def process_messages(arrival_times):
    # 队列的最大长度
    max_queue_length = 3
    # 每个队列的处理时间
    queue_1_time = 1
    queue_2_time = 2

    # 初始化两个队列，队列的每个元素是一个时间戳，表示该消息的处理完成时间
    queue_1 = deque()
    queue_2 = deque()

    # 当前时间
    current_time = 0
    # 记录最后一个消息处理完成的时间
    last_processed_time = 0

    for arrival_time in arrival_times:
        # 先处理队列中已完成的消息
        # 清理队列1
        while queue_1 and queue_1[0] <= arrival_time:
            queue_1.popleft()
        # 清理队列2
        while queue_2 and queue_2[0] <= arrival_time:
            queue_2.popleft()

        # 决定将消息放入哪个队列
        if len(queue_1) < len(queue_2):  # 如果队列1较短
            queue_1.append(max(arrival_time, current_time) + queue_1_time)
            last_processed_time = queue_1[-1]
        elif len(queue_1) > len(queue_2):  # 如果队列2较短
            queue_2.append(max(arrival_time, current_time) + queue_2_time)
            last_processed_time = queue_2[-1]
        else:  # 如果两个队列一样长，优先选择处理速度快的队列
            queue_1.append(max(arrival_time, current_time) + queue_1_time)
            last_processed_time = queue_1[-1]

        # 更新当前时间
        current_time = arrival_time

    return last_processed_time


# 测试用例
arrival_times = [0, 0, 0, 0, 0, 1, 1, 2, 2]
last_time = process_messages(arrival_times)
print(f"最后一个消息的处理完成时间为: {last_time}秒")
