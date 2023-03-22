#  소인수분해

N = int(input())
N_ori = N
tmp = 2
while N != 1:
    if N % tmp == 0:
        print(tmp)
        N /= tmp
    else:
        tmp += 1
