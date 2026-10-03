numbers = [10, 25, 7, 40, 18, 40, 32]

unique_numbers = list(set(numbers))
unique_numbers.sort()

second_largest = unique_numbers[-2]

print("Second largest number:", second_largest)
