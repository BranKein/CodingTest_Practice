#  골드바흐의 추측
#  @date 22.Mar.2023
#  @link https://www.acmicpc.net/problem/6588


input_list = list()
biggest = 1000000

prime_list_bool = [True] * (biggest + 1)
prime_list_bool[0] = False
prime_list_bool[1] = False

prime_list = list()

for i in range(2, int(pow(biggest, 0.5)) + 1):
    if prime_list_bool[i]:
        for j in range(i+i, biggest+1, i):
            prime_list_bool[j] = False
        prime_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break

    found = False
    for prime in prime_list[1:]:
        if prime > n:
            break
        if prime_list_bool[n - prime]:
            print("{} = {} + {}".format(n, prime, n - prime))
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")
