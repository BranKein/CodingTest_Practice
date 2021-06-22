def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(participant)):
        if participant[i] != completion[i] or i == len(participant) - 1:
            return participant[i]
