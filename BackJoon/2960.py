#  에라토스테네스의 체


input_line = input().split(' ')
N = int(input_line[0])
K = int(input_line[1])

prime_list_bool = [True] * (N + 1)
prime_list = list()
for i in range(2, N+1):
    if prime_list_bool[i]:
        for j in range(i, N+1, i):
            if prime_list_bool[j]:
                K -= 1
                prime_list_bool[j] = False
            if K == 0:
                print(j)
                break
    if K == 0:
        break
