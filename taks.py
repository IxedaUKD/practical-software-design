import time


def is_prime(num):
    """Checking if a number is prime"""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_num_generator():
    """Generator of prime numbers"""
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1



def timer_wrapper(func):
    """Decorator for measuring the execution time of a function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Час виконання: {execution_time:.4f} секунд")
        return result
    return wrapper

@timer_wrapper
def prime_num_getter(n):
    """Obtaining n prime numbers."""
    prime_gen = prime_num_generator()
    primes = [next(prime_gen) for _ in range(n)]
    print(f"Перші {n} простих чисел: {primes}")



prime_num_getter(10)
