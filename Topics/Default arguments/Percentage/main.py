def get_percentage(number, round_digits=None):
    if isinstance(round_digits, int) and round_digits >= 0:
        return f"{round(number * 100., round_digits)}%"
    else:
        return f"{int(number * 100)}%"
