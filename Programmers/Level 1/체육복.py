def solution(n, lost, reserve):
    clothes = [1] * n
    for i in lost:
        clothes[i - 1] -= 1
    for i in reserve:
        clothes[i - 1] += 1

    for i in range(len(clothes)):
        if clothes[i] == 2:
            if i == 0:
                if clothes[i + 1] == 0:
                    clothes[i] -= 1
                    clothes[i + 1] += 1
            elif i == len(clothes) - 1:
                if clothes[i - 1] == 0:
                    clothes[i] -= 1
                    clothes[i - 1] += 1
            else:
                if clothes[i - 1] == 0:
                    clothes[i] -= 1
                    clothes[i - 1] += 1
                elif clothes[i + 1] == 0:
                    clothes[i] -= 1
                    clothes[i + 1] += 1

    # print(clothes)
    answer = 0
    for cloth in clothes:
        if cloth > 0:
            answer += 1
    return answer
