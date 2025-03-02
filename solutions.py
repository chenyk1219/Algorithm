from collections import deque
from queue import LifoQueue, SimpleQueue


def solutions(msg_list):
    queue1 = []
    queue2 = []
    max_length = 3
    msg = deque(msg_list)
    # print(msg, len(msg))
    finsh_time = []

    current_time = 0
    while msg:
        while queue1 and queue1[-1] <= current_time:
            queue1.pop()
        while queue2 and queue2[-1] <= current_time:
            queue2.pop()
        while msg and msg[0] <= current_time:
            # print("msg[0] is: ", msg[0])
            # if len(queue1) == len(queue2) == 3:
            #     break
            if len(queue1) < max_length and len(queue1) <= len(queue2):
                # print("in to 11111")
                queue1.append(max(msg[0], current_time) + 1)
                finsh_time.append(max(msg[0], current_time) + 1)
            else:
                # print("in to 22222")
                queue2.append(max(msg[0], current_time) + 2)
                finsh_time.append(max(msg[0], current_time) + 2)
            msg.popleft()
        current_time += 1
    print(finsh_time)
    return max(finsh_time)


arrival_times = [0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2]
print(arrival_times)
last_time = solutions(arrival_times)
print(f"最后一个消息的处理完成时间为: {last_time}秒")
