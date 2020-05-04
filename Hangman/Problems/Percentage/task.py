def get_percentage(number, precision=0):
    if precision == 0:
        return str(round(number * 100)) + '%'
    return str(round(number * 100, precision)) + '%'
