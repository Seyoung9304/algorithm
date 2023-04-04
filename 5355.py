T = int(input())
for _ in range(T):
    line = input().split()
    n = float(line[0])
    for op in line[1:]:
        if op=="@":
            n *= 3
        elif op=="%":
            n += 5
        elif op=="#":
            n -= 7
    print("{0:0.2f}".format(n))