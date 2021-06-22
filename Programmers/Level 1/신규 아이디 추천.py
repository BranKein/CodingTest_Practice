def solution(new_id):
    # 1단계
    new_id = new_id.lower()
    new_id = list(new_id)
    # 2단계
    new_id_list = list()
    for char in new_id:
        if char >= 'A' and char <= 'Z':
            new_id_list.append(char)
            continue
        elif char >= 'a' and char <= 'z':
            new_id_list.append(char)
            continue
        elif char >= '0' and char <= '9':
            new_id_list.append(char)
            continue
        elif char == '-' or char == '_' or char == '.':
            new_id_list.append(char)
            continue
    # 3단계
    dot_flag = False
    new_id = list()
    for char in new_id_list:
        if char == '.':
            if not dot_flag:
                new_id.append(char)
                dot_flag = True
        else:
            new_id.append(char)
            dot_flag = False
    # 4단계
    if len(new_id) > 0:
        if new_id[0] == '.':
            del new_id[0]
    if len(new_id) > 0:
        if new_id[-1] == '.':
            del new_id[-1]
    # 5단계
    if len(new_id) == 0:
        new_id.append('a')
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            del new_id[-1]
    # 7단계
    if len(new_id) <= 2:
        char = new_id[-1]
        for i in range(3 - len(new_id)):
            new_id.append(char)

    print(new_id)

    answer = ''
    for char in new_id:
        answer += char
    return answer