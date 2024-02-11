'''
    Замикання в програмуванні - це функція, яка зберігає посилання на змінні зі свого 
    лексичного контексту, тобто з області, де вона була оголошена.

    Реалізуйте функцію caching_fibonacci, яка створює та використовує кеш для зберігання і 
    повторного використання вже обчислених значень чисел Фібоначчі.

    Ряд Фібоначчі - це послідовність чисел виду: 0, 1, 1, 2, 3, 5, 8, ..., де кожне наступне 
    число послідовності виходить додаванням двох попередніх членів ряду.

    У загальному вигляді для обчислення n-го члена ряду Фібоначчі потрібно вирахувати вираз: 
    Fn = Fn-1 + Fn-2

    Це завдання можна вирішити рекурсивно, викликаючи функцію, що обчислює числа 
    послідовності доти, доки виклик не сягне членів ряду менше n = 1, де послідовність задана.
'''

def caching_fibonacci() -> callable:
    """Returns a function that calculates the Fibonacci sequence with caching."""
    cache = {}
    
    def fibonacci(n: int) -> int:
        """Calculates the Fibonacci number for a given index."""        
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cache:
            return cache[n]
        
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Test
# fib = caching_fibonacci()
# print(fib(10)) # 55
# print(fib(15)) # 610

###################################################################################################
###################################################################################################
###################################################################################################

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
    pattern = r'\s\d+\d.\d+\s'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    """Sum the numbers extracted using the provided function."""
    return sum(func(text))

# Test
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

###################################################################################################
###################################################################################################
###################################################################################################

'''
    Розробіть Python-скрипт для аналізу файлів логів. Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка, і виводити статистику за рівнями логування наприклад, INFO, ERROR, DEBUG. Також користувач може вказати рівень логування як другий аргумент командного рядка, щоб отримати всі записи цього рівня.

    Файли логів – це файли, що містять записи про події, які відбулися в операційній системі, програмному забезпеченні або інших системах. Вони допомагають відстежувати та аналізувати поведінку системи, виявляти та діагностувати проблеми.

    Для виконання завдання візьміть наступний приклад лог-файлу:

    2024-01-22 08:30:01 INFO User logged in successfully.
    2024-01-22 08:45:23 DEBUG Attempting to connect to the database.
    2024-01-22 09:00:45 ERROR Database connection failed.
    2024-01-22 09:15:10 INFO Data export completed.
    2024-01-22 10:30:55 WARNING Disk usage above 80%.
    2024-01-22 11:05:00 DEBUG Starting data backup process.
    2024-01-22 11:30:15 ERROR Backup process failed.
    2024-01-22 12:00:00 INFO User logged out.
    2024-01-22 12:45:05 DEBUG Checking system health.
    2024-01-22 13:30:30 INFO Scheduled maintenance.
'''

import sys


def parse_log_line(line: str) -> dict:
    """Parse a log line and return a dictionary with date, time, level, and message."""
    parts = line.split(maxsplit=3)
    return {
        'date': parts[0], 
        'time': parts[1], 
        'level': parts[2], 
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    """Load logs from a file and return a list of log dictionaries."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except Exception as e:
        print(f"Exception: {e}")   
    return logs

def count_logs_by_level(logs: list) -> dict:
    """Count logs by level and return a dictionary with counts for each level."""
    counts = {'INFO': 0, 'ERROR': 0, 'DEBUG': 0, 'WARNING': 0}
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict) -> None:
    """Print log level counts."""
    print("Log Level   |   Count")
    print("---------------------")
    for level, count in counts.items():
        print(f"{level.ljust(11)} |   {count}")

def show_logs_by_level(logs: list, level: str) -> list:
    """Print details of logs for the specified level."""
    filtered_logs = [log for log in logs if log['level'] == level.upper()]
    print(f"\nDetails of logs for level '{level.upper()}':")
    for log in filtered_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")

def main(file_path: str, level: str = None) -> None:
    """Main function to analyze log files."""
    logs = load_logs(file_path)

    if not logs:
        return
    
    counts = count_logs_by_level(logs)
    display_log_counts(counts)
    
    if level:
        show_logs_by_level(logs, level)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <file_path> [<level>]")
    else:
        file_path = sys.argv[1]
        level = sys.argv[2] if len(sys.argv) > 2 else None
        main(file_path, level)
    

###################################################################################################
###################################################################################################
###################################################################################################
    
'''
    Доробіть консольного бота помічника з попереднього домашнього завдання та 
    додайте обробку помилок за допомоги декораторів.

    Вимоги до завдання:

    Всі помилки введення користувача повинні оброблятися за допомогою декоратора 
    input_error. Цей декоратор відповідає за повернення користувачеві повідомлень 
    типу "Enter user name", "Give me name and phone please" тощо.
    Декоратор input_error повинен обробляти винятки, що виникають у функціях - 
    handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається 
    виняток декоратор повинен повертати відповідну відповідь користувачеві. 
    Виконання програми при цьому не припиняється.
'''

'''
    Доробіть консольного бота помічника з попереднього домашнього завдання та 
    додайте обробку помилок за допомоги декораторів.

    Вимоги до завдання:

    Всі помилки введення користувача повинні оброблятися за допомогою декоратора 
    input_error. Цей декоратор відповідає за повернення користувачеві повідомлень 
    типу "Enter user name", "Give me name and phone please" тощо.
    Декоратор input_error повинен обробляти винятки, що виникають у функціях - 
    handler і це винятки: KeyError, ValueError, IndexError. Коли відбувається 
    виняток декоратор повинен повертати відповідну відповідь користувачеві. 
    Виконання програми при цьому не припиняється.
'''

def input_error(func):
    """Decorator function to handle input errors."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        
        except KeyError:
            return 'Error: Key not found.'
        except ValueError:
            return 'Error: Invalid input format. Please provide the correct argument(s).'
        except IndexError:
            return 'Error: Insufficient arguments. Please provide the correct argument(s).'
        except Exception as e:
            return f'Error: {str(e)}. Please check your input and try again.'
        
    return inner

@input_error
def parse_input(user_input: str) -> tuple[str, ...]:
    """Parse user input and return a tuple with command and arguments."""
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    """Add a new contact to the contacts dictionary."""
    name, phone = args
    if name in contacts:
        return f"Contact '{name}' already exists. Use 'change' command to update."
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args: tuple[str, str], contacts: dict[str, str]) -> str:
    """Update a contact in the contacts dictionary."""
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found. Use 'add' command to create a new contact."
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args: tuple[str], contacts: dict[str, str]) -> str:
    """Show the phone number of a contact."""
    name = args[0]
    return contacts.get(name, "The name wasn`t found.")

@input_error    
def show_all(contacts: dict[str, str]) -> dict[str, str]:
    return contacts   

def main():
    """Main function to interact with the assistant bot."""
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        
        if command in ['close', 'exit']:
            print("Good Bye!")
            break    
        elif command == 'hello':
            print("How can i help you?")
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == '__main__':
    main()