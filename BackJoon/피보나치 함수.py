def fibonacci_with_memo(memo, n):
    if memo[n] != (-1, -1):
        return memo[n]
    elif n == 0:
        return 1, 0
    elif n == 1:
        return 0, 1
    else:
        zero_1, one_1 = fibonacci_with_memo(memo, n - 1)
        zero_2, one_2 = fibonacci_with_memo(memo, n - 2)
        memo[n] = (zero_1 + zero_2, one_1 + one_2)
        return memo[n]


memo = list()
for i in range(41):
    memo.append((-1, -1))
memo[0] = (1, 0)
memo[1] = (0, 1)

n = int(input())
for i in range(n):
    zero, one = fibonacci_with_memo(memo, int(input()))
    print("{} {}".format(zero, one))
