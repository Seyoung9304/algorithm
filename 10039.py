s_sum = 0
NUM_ITER = 5
for _ in range(NUM_ITER):
    s = int(input())
    s_sum += (s if s>40 else 40)
print(s_sum//NUM_ITER)