import re
from typing import Callable

def generator_numbers(text: str):
    # Пошук всіх дійсних чисел у тексті
    for match in re.finditer(r"\b\d+\.\d+\b", text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    total = sum(
        func(text)
    )  
    return total


# Приклад використання:
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")