#  수 정렬하기 2


N = int(input())
if_num = False
num_list_pos = list()
num_list_neg = list()
max_num_pos = 0
max_num_neg = 0

for i in range(N):
    tmp = int(input())
    if tmp == 0:
        if_num = True
    elif tmp > 0:
        if tmp > max_num_pos:
            max_num_pos = tmp
        num_list_pos.append(tmp)
    else:
        tmp = abs(tmp)
        if tmp > max_num_neg:
            max_num_neg = tmp
        num_list_neg.append(tmp)

if max_num_pos > 0:
    counting_pos = [0] * max_num_pos
    for i in range(len(num_list_pos)):
        counting_pos[num_list_pos[i] - 1] += 1
    for i in range(1, max_num_pos):
        counting_pos[i] += counting_pos[i - 1]

    result_list_pos = [0] * len(num_list_pos)

    for i in range(len(num_list_pos) - 1, -1, -1):
        result_list_pos[counting_pos[num_list_pos[i] - 1] - 1] = num_list_pos[i]
        counting_pos[num_list_pos[i] - 1] -= 1
if max_num_neg > 0:
    counting_neg = [0] * max_num_neg
    for i in range(len(num_list_neg)):
        counting_neg[num_list_neg[i] - 1] += 1
    for i in range(1, max_num_neg):
        counting_neg[i] += counting_neg[i - 1]

    result_list_neg = [0] * len(num_list_neg)

    for i in range(len(num_list_neg) - 1, -1, -1):
        result_list_neg[counting_neg[num_list_neg[i] - 1] - 1] = num_list_neg[i]
        counting_neg[num_list_neg[i] - 1] -= 1

for i in range(len(num_list_neg) - 1, -1, -1):
    print(-result_list_neg[i])
if if_num:
    print(0)
for i in range(len(num_list_pos)):
    print(result_list_pos[i])
