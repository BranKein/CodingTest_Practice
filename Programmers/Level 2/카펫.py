def solution(brown, yellow):
    whole = brown + yellow
    answer = []
    for i in range(2, whole):
        if whole % i == 0:
            l = i
            w = whole / i
            if (l-2) * (w-2) == yellow:
                answer.append(max(l, w))
                answer.append(min(l, w))
                break
    return answer
