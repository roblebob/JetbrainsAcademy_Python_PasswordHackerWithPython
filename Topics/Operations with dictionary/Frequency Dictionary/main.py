# put your python code here
text = input()
words = list(set(map(lambda s: s.lower(), text.split())))
statistic = {word: text.lower().split().count(word) for word in words}
for key, value in statistic.items():
    print(key, value)