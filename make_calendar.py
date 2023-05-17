def make_calendar(year):
    calender = {
        'jan': [], 'feb': [], 'mar': [], 'apr': [], 'may': [], 'jun': [],
        'jul': [], 'aug': [], 'sep': [], 'oct': [], 'nov': [], 'dec': []
    }
    for i in range(1, 32):
        calender['jan'].append(i)
        calender['mar'].append(i)
        calender['may'].append(i)
        calender['jul'].append(i)
        calender['aug'].append(i)
        calender['oct'].append(i)
        calender['dec'].append(i)

    for i in range(1, 31):
        calender['apr'].append(i)
        calender['jun'].append(i)
        calender['sep'].append(i)
        calender['nov'].append(i)

    if year % 4 == 0:
        for i in range(1, 30):
            calender['feb'].append(i)
    else:
        for i in range(1, 29):
            calender['feb'].append(i)

    return calender

