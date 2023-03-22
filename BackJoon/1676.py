#  팩토리얼 0의 개수


num = int(input())

two = 0
five = 0
for i in range(1, num+1):
    tmp = i
    while True:
        if tmp % 2 == 0:
            two += 1
            tmp /= 2
        if tmp % 5 == 0:
            five += 1
            tmp /= 5
        if tmp % 2 != 0 and tmp % 5 != 0:
            break
print(min(two, five))
