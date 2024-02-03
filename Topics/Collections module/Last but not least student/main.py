# the following line reads a dict from the input and converts it into an OrderedDict, do not modify it, please
marks = OrderedDict(json.loads(input()))

# your code here
name = "Max"
marks[name] = 100
marks.move_to_end(name, last=False)
print(marks)
