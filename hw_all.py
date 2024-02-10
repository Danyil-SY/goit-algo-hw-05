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

def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
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
    pattern = r'\b\d+\.\d+\b'
    for match in re.findall(pattern, text):
        yield float(match)

def sum_profit(text: str, func: Callable):
    return sum(func(text))

# Test
# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
# total_income = sum_profit(text, generator_numbers)
# print(f"Загальний дохід: {total_income}")

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

def input_error(func):
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
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    name = args[0]
    return contacts.get(name, "The name wasn`t found.")

@input_error    
def show_all(contacts):
    return contacts   

def main():
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
            print("Invalid command")

if __name__ == '__main__':
    main()