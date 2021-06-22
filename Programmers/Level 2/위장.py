def solution(clothes):
    data = dict()
    for i in clothes:
        if i[1] not in data:
            data[i[1]] = 1
        else:
            data[i[1]] += 1

    answer = 1
    items_list = list()
    for i in data.items():
        items_list.append(i[1])
    for i in items_list:
        answer *= (i + 1)
    return answer - 1
