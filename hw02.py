'''
    Необхідно створити функцію generator_numbers, яка буде аналізувати текст, 
    ідентифікувати всі дійсні числа, що вважаються частинами доходів, і 
    повертати їх як генератор. Дійсні числа у тексті записані без помилок, 
    чітко відокремлені пробілами з обох боків. Також потрібно реалізувати 
    функцію sum_profit, яка буде використовувати generator_numbers для 
    підсумовування цих чисел і обчислення загального прибутку.
'''

import re
from typing import Callable


def generator_numbers(text: str):
    """Generator function to extract floating-point numbers from a text."""
    pattern = r'\s\d+\.\d+\s'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    """Sum the numbers extracted using the provided function."""
    return round(sum(func(text)), 2)

# Test
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")