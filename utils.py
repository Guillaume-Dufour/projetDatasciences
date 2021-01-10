def month(str_month):
    values = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": "05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12"
    }

    return values.get(str_month.lower())


def two_digit_string(string):
    return "0" + string if len(string) == 1 else string
