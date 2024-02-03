# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
firms = OrderedDict(json.loads(input()))

for _ in range(2):
    firms.popitem(last=True)

print(firms)