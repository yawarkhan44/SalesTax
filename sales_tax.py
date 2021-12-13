
from math import ceil



def calculate_rounded_tax(amount):
    return ceil(round(amount , 2) * 20) / 20
