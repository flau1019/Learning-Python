
monthConversion = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    1 : "october",
    2 : "november",
    3 : "december"
}

print(monthConversion.get("jan"))

monthConversion.update({4:"march"})

print(monthConversion.get(4))