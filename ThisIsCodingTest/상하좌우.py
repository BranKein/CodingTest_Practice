n = int(input())
line = input().split(' ')
pos = list([1, 1])

for c in line:
    if c == 'R':
        if pos[1] != n:
            pos[1] += 1
    elif c == 'L':
        if pos[1] != 1:
            pos[1] -= 1
    elif c == 'U':
        if pos[0] != 1:
            pos[0] -= 1
    elif c == 'D':
        if pos[0] != n:
            pos[0] += 1

print("{} {}".format(pos[0], pos[1]))
