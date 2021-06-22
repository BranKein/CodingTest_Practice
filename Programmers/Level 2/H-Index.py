def solution(citations):
    citations.sort()
    for i in range(len(citations)+2):
        tmp = 0
        # i번 이상 인용된 논문 개수
        for j in citations:
            if j >= i:
                tmp += 1
        # 논문 개수가 i보다 작으면 조건 만족 안함 -> i-1이 답
        if i > tmp:
            return i-1
    return 0
