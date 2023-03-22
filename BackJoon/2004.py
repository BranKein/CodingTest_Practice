#  조합 0의 개수


def countNum(N, num):
    count = 0
    divNum = num
    while N >= divNum:
        count += N // divNum
        divNum *= num
    return count


inputLine = input().split(' ')
n = int(inputLine[0])
m = int(inputLine[1])
print(min((countNum(n, 2) - countNum(m, 2) - countNum(n-m, 2)), (countNum(n, 5) - countNum(m, 5) - countNum(n-m, 5))))
