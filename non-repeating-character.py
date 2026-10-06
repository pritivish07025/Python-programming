def first_non_repeating(s):
    count = {}

    # Count frequency of each character
    for ch in s:
        count[ch] = count.get(ch, 0) + 1

    # Find the first character with frequency 1
    for ch in s:
        if count[ch] == 1:
            return ch

    return None


s = input("Enter a string: ")

result = first_non_repeating(s)

if result:
    print("First non-repeating character:", result)
else:
    print("No non-repeating character found")
