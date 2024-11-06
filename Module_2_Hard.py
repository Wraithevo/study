n = int(input())
result = 0
for i in range(1, 20):
    for p in range(i+1, 20):
        if n % (p + i) == 0:
            result = str(result) + str(i) + str(p)
print(int(result))
