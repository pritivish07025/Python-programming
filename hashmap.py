nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

seen = {}

for i in range(len(nums)):
    complement = target - nums[i]

    if complement in seen:
        print("Indices:", seen[complement], i)
        break

    seen[nums[i]] = i
else:
    print("No pair found")
