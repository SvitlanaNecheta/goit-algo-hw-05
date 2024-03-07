import re
from typing import Callable
from decimal import getcontext, Decimal


def generator_numbers(text: str):
    for word in text.split():
        if re.fullmatch(r"\d+[.]+\d+",word):
            yield float(word)


def sum_profit(text: str, func: Callable):
    sum = 0
    getcontext().prec = 6
    for n in func:
        sum += Decimal(n)
    return sum





    
      
  

