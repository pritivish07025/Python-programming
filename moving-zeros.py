
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = []
zero_count = 0

for num in numbers:
    if num == 0:
        zero_count += 1
    else:
        result.append(num)

result.extend([0] * zero_count)

print("Updated list:", result)
