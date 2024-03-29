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