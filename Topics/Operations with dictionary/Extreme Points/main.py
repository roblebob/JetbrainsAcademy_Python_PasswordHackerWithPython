# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
ordered = sorted(test_dict.items(), key=lambda x: x[1])
print(f"min: {ordered[0][0]}")
print(f"max: {ordered[-1][0]}")