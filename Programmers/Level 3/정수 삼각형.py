def solution(triangle):
    sumList = list()
    for line in triangle:
        Line = list()
        for i in line:
            Line.append(-1)
        sumList.append(Line)

    for i in range(len(triangle[-1])):
        sumList[-1][i] = triangle[-1][i]

    def maxSum(i, j):
        if sumList[i][j] != -1:
            return sumList[i][j]
        else:
            sumList[i][j] = triangle[i][j] + max(maxSum(i + 1, j), maxSum(i + 1, j + 1))
            return sumList[i][j]

    answer = maxSum(0, 0)
    return answer
