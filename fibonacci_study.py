
# memoization:

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1} # base

def fib1(n: int) -> int:
    if n not in memo:
        memo[n] = fib1(n - 1) + (n - 2)
    return memo[n]

if __name__ == '__main__':
    print(fib1(8))
    print(fib1(50))

# automatic memoization:

from functools import lru_cache

@lru_cache(maxsize = None)
def fib2(n: int) -> int:
    if n < 2: # base
        return n
    return fib2(n - 1) + (n - 2) # recursive

if __name__ == '__main__':
    print(fib2(5))
    print(fib2(50))

# simplest way

def fib3(n: int) -> int:
    if n == 0: return n          # special case
    last: int = 0                # fib(0) previously defined
    next: int = 1                # fib(1) previously defined
    for _ in range(1, n):        # tuples dispatch
        last, next = next, last + next
    return next

if __name__ == '__main__':
    print(fib3(10))
    print(fib3(50))

# fibonacci generator (show the sequence and not just a single value)

from typing import Generator

def fib4(n: int) -> Generator[int, None, None]:
    yield 0                         # special case
    if n > 0: yield 1               # special case
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next

if __name__ == '__main__':
    for i in fib4(50):
        print(i)