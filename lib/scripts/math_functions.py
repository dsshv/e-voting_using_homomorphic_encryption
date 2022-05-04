import random
import math


def lFunction(argument_extension: int, modulus: int):
    return (argument_extension - 1) // modulus


# True test that number is prime, but to long
# def checkingNumberIsPrime(number: int):
#     k = 0
#     for i in range(2, number // 2 + 1):
#         if number % i == 0:
#             k = k + 1
#     if k <= 0:
#         return False
#     else:
#         return True


def generating_number_prime(left: int, right: int):
    modulus_p: int = random.randint(left, right)
    while not isPrime(number=modulus_p):
        modulus_p = random.randint(left, right)
    return modulus_p


#  extended Euclid algorithm
def gcdExtended(num1: int, num2: int):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcdExtended(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def power_mod(x: int, y: int, p: int):
    res = 1
    x = x % p
    while y > 0:
        if y & 1:
            res = (res * x) % p
        y = y >> 1
        x = (x * x) % p
    return res


# Miller-Rabin primary test
def isPrime(number: int, k=2000):
    def millerTest(d, n):
        a = 2 + random.randint(1, n - 4)
        x = power_mod(a, d, n)
        if x == 1 or x == n - 1:
            return True

        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False

    if number <= 1 or number == 4:
        return False
    if number <= 3:
        return True
    d = number - 1
    while d % 2 == 0:
        d //= 2
    for i in range(k):
        if not millerTest(d, number):
            return False
    return True


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def primitive_root(modulo):
    required_set = set(num for num in range(1, modulo) if gcd(num, modulo) == 1)
    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range(1, modulo))
        if required_set == actual_set:
            return g
