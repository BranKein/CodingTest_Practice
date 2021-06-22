N = int(input())
num_list = list()
for i in range(N):
    num_list.append(int(input()))
num_list.sort()
for i in num_list:
    print(i)
