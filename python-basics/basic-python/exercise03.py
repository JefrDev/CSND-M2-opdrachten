numbers = [4, 20, 10, 18, 9, 17, 11, 15]
strings = ["18", "15", "5", "6", "10", "16", "11", "8"]

result = []

# Add your code here.
for number in numbers:
    if number % 3 == 0:
        result.append(number)
result *= 3

for string in strings:
    if len(string) == 2:
        string = int(string)
        if string == 16:
            break
        result.append(string)

print(result)
