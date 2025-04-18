#Project2: Write 3 different apps that find the highest prime number in a given duration and n, 
# And then calculate the fibonacci and factorial of that number using the 3 different concurrency models:
# 1. Multiprocessing app        
# 2. Threading app
# 3. Async app
# Author: Hermann Kenko Tanfoudie
# Date: 04/4/2025

import time
import asyncio
import multiprocessing
import threading
import math

# Let define the prime number function 
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Let define the highest prime number function for the given duration and n
def highest_prime(duration=10):
    
 start_time = time.time()
 n = 0
 highest_primeNum = 2
 while  time.time() - start_time < duration:
        if is_prime(n):
            highest_primeNum = n
        n += 1
 return math.highest_primeNum

# Let define the factorial function for the highest prime number
def factorial(n):
    n = highest_prime
    return math.factorial(n)

#let define the fibonacci function for the highest prime number
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]

    fibonacci(n) == fibonacci(n-1, memo) + fibonacci(n-2, memo)
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return memo[n]
    
# Let define the multiprocessing function
def multiprocess_app():
    prime = highest_prime()
    print(f"Highest Prime number multiprocessed found: {prime}")
    with multiprocessing.Pool(processes=2) as pool:
        fib_result = pool.apply_async(fibonacci, args=(prime,))
        fact_result = pool.apply_async(factorial, args=(prime,))
        return prime, fib_result.get(), fact_result.get()

# Let define the threading function
def threaded_app():
    results = {}

    def find_prime():
        results['prime'] = highest_prime()

    prime_thread = threading.Thread(target=find_prime)
    prime_thread.start()
    prime_thread.join()

    def run_fib():
        results['fibonacci'] = fibonacci(results['prime'])

    def run_fact():
        results['factorial'] = factorial(results['prime'])

    fib_thread = threading.Thread(target=run_fib)
    fact_thread = threading.Thread(target=run_fact)
    fib_thread.start()
    fact_thread.start()
    fib_thread.join()
    fact_thread.join()

    return results['prime'], results['fibonacci'], results['factorial']

# Let define the async function
async def async_find_highest_prime():
    start_time = time.time()
    n = 0
    last_prime = 2
    while time.time() - start_time < 180:
        if is_prime(n):
            last_prime = n
        n += 1
        if n % 1000 == 0:
            await asyncio.sleep(0)  # Yield control
    return last_prime

async def async_fibonacci(n):
    return fibonacci(n)

async def async_factorial(n):
    return factorial(n)

async def async_app():
    prime = await async_find_highest_prime()
    print(f"[Async] Highest prime found: {prime}")
    fib_task = asyncio.create_task(async_fibonacci(prime))
    fact_task = asyncio.create_task(async_factorial(prime))
    fib_result = await fib_task
    fact_result = await fact_task
    return prime, fib_result, fact_result

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run different concurrency models.")
    parser.add_argument("mode", choices=["multi", "thread", "async"], help="Concurrency mode to run")
    args = parser.parse_args()

    if args.mode == "multi":
        prime, fib, fact = multiprocess_app()
    elif args.mode == "thread":
        prime, fib, fact = threaded_app()
    elif args.mode == "async":
        prime, fib, fact = asyncio.run(async_app())

    print(f"\nPrime: {prime}\nFibonacci({prime}): [Length: {len(str(fib))} digits]\nFactorial({prime}): [Too large to display] (Length: {len(str(fact))} digits)")


    
