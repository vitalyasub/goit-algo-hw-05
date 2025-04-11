def caching_fibonacci():
    cache = {}  # Словник для збереження обчислених значень

    def fibonacci(n):
        # Базові випадки
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевірка, чи вже є значення в кеші
        if n in cache:
            return cache[n]

        # Рекурсивне обчислення з кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

fib = caching_fibonacci()
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610