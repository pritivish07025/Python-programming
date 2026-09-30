numbers = [10, 25, 8, 45, 32, 45]

# Remove duplicates
unique_numbers = list(set(numbers))

# Sort in descending order
unique_numbers.sort(reverse=True)

if len(unique_numbers) >= 2:
    print("Second largest number:", unique_numbers[1])
else:
    print("Second largest number does not exist")
