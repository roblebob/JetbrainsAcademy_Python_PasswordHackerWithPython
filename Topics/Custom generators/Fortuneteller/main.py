def counter(s: str):
    count = 0
    for digit in s:
        count += int(digit)
        yield count


my_gen = counter(input())
result = 0
for i in my_gen:
    result = i

print(result)

