def fibonacci(n):
    past = []
    for i in range(n):
        cond = i < 2
        result = i if cond else past[1] + past[0]
        yield result
        past.append(result)
        if not cond:
            past.pop(0)
