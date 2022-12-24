from datetime import datetime

from numba import njit

import example


def fact(n: int) -> int:
    if n <= 1:
        return 1;
    else:
        return n*fact(n-1);


def prime(n: int) -> int:
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


def idle():
    pass


import numexpr as ne
def numexpr_prime(n: int) -> int:
    for i in range(2, n):
        if ne.evaluate('n % i == 0'):
            return 0
    return 1


@njit()
def numba_prime(n: int) -> int:
    for i in range(2, n):
        if n % i == 0:
            return 0
    return 1


@njit()
def numba_idle():
    pass


def tight_loops():
    print("==============================")
    runs = 3
    # n =              13
    # n =           1_009
    # n =       6_700_417
    # n =       2_097_593
    n =      55_555_553
    # n =     999_999_937
    # n =   2_147_483_647
    # n = 999_999_000_001

    for i in range(runs):
        print("******************************")
        start = datetime.now()
        py = prime(n)
        pytime = datetime.now() - start
        print(f"Python got {py} in {pytime}")

        # start = datetime.now()
        # e = numexpr_prime(n)
        # numexprtime = datetime.now() - start
        # print(f"Numexpr got {e} in {numexprtime}")

        start = datetime.now()
        b = numba_prime(n)
        numbatime = datetime.now() - start
        print(f"Numba  got {b} in {numbatime}")

        start = datetime.now()
        c = example.prime(n)
        ctime = datetime.now() - start
        print(f"C      got {c} in {ctime}")

        print(f"Numba  is {(pytime / numbatime)} times faster")
        print(f"C      is {(pytime / ctime)} times faster")
        print("******************************")

    print("==============================")



def call_func(times, func, param) -> int:
    for i in range(times):
        func(param)
    return func(param)


def many_function_calls():
    print("==============================")
    runs = 3

    for i in range(runs):
        print("******************************")
        times = 10000000
        n = 2

        start = datetime.now()
        py = call_func(times, prime, n)
        pytime = datetime.now() - start
        print(f"Python got {py} in {pytime}")

        # start = datetime.now()
        # e = call_func(times, numexpr_prime, n)
        # numexprtime = datetime.now() - start
        # print(f"Numexpr got {e} in {numexprtime}")

        start = datetime.now()
        b = call_func(times, numba_prime, n)
        numbatime = datetime.now() - start
        print(f"Numba  got {b} in {numbatime}")

        start = datetime.now()
        c = call_func(times, example.prime, n)
        ctime = datetime.now() - start
        print(f"C     got {c} in {ctime}")

        print(f"Numba  is {(pytime / numbatime)} times faster")
        print(f"C      is {(pytime / ctime)} times faster")
        print("******************************")
    print("==============================")



def call_empty_function(times, func):
    for i in range(times):
        func()


def many_empty_function_calls():
    print("==============================")
    runs = 3

    for i in range(runs):
        print("******************************")
        times = 1000000

        start = datetime.now()
        call_empty_function(times, idle)
        pytime = datetime.now() - start
        print(f"Python: {pytime}")

        # start = datetime.now()
        # e = call_func(times, numexpr_prime, n)
        # numexprtime = datetime.now() - start
        # print(f"Numexpr got {e} in {numexprtime}")

        start = datetime.now()
        call_empty_function(times, numba_idle)
        numbatime = datetime.now() - start
        print(f"Numba : {numbatime}")

        start = datetime.now()
        call_empty_function(times, example.idle)
        ctime = datetime.now() - start
        print(f"C     : {ctime}")
        print("******************************")

    print("==============================")



def main():
    tight_loops()
    # many_function_calls()
    # many_empty_function_calls()


if __name__ == '__main__':
    main()
