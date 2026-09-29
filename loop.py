A = [2, 4, 6, 8, 10]

result = []

for i in range(len(A)):
    if A[i] % 4 == 0:
        result.append(A[i] // 2)
    else:
        result.append(A[i] + 1)

print(result)
