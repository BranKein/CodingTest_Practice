import math


def solution(progresses, speeds):
    days = list()
    for i in zip(progresses, speeds):
        days.append(math.ceil((100-i[0])/i[1]))
    time = days[0]
    for i in range(len(days)):
        if days[i] <= time:
            days[i] = time
        else:
            time = days[i]
    tmp = days[0]
    count = 0
    answer = []
    for day in days:
        if tmp == day:
            count += 1
        else:
            answer.append(count)
            tmp = day
            count = 1
    answer.append(count)
    return answer
