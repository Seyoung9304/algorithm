h, m, s = map(int, input().split())
c = int(input())

# second
s += c
if s >= 60:
    m += (s // 60)
    s %= 60
# minute
if m >= 60:
    h += (m // 60)
    m %= 60
# hour
h %= 24

print(h, m, s)