#  골드바흐의 추측


input_list = list()
num = 0
while True:
    n = int(input())
    if n == 0:
        break
    else:
        input_list.append(n)
        if num < n:
            num = n

prime_list_bool = [True] * (num + 1)
prime_list = list()
for i in range(2, num // 2 + 1):
    if prime_list_bool[i]:
        for j in range(i+i, num, i):
            prime_list_bool[j] = False

for i in range(2, num):
    if prime_list_bool[i]:
        prime_list.append(i)

for j in input_list:
    found = False
    for i in range(j // 2 + 1):
        if prime_list_bool[j - prime_list[i]]:
            print("{} = {} + {}".format(j, prime_list[i], j - prime_list[i]))
            found = True
            break
    if not found:
        print("Goldbach's conjecture is wrong.")
