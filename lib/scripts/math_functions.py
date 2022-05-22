import random


def l_function(argument_extension: int, modulus: int):
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
    generated_prime: int = random.randint(left, right)
    while not is_prime(number=generated_prime):
        generated_prime = random.randint(left, right)
    return generated_prime


#  extended Euclid algorithm
def gcd_extended(num1: int, num2: int):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = gcd_extended(num2 % num1, num1)
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
def is_prime(number: int, k=2000):
    def miller_rabin_test(d, n):
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
        if not miller_rabin_test(d, number):
            return False
    return True

# def primitive_root(modulo):
#     montgomery = mr.MontgomeryReducer(modulo)
#     required_set = set(num for num in range(1, modulo) if gcd_extended(num, modulo)[0] == 1)
#     for g in range(1, modulo):
#         actual_set = set(montgomery.montgomery_pow(g, powers) for powers in range(1, modulo))
#         if required_set == actual_set:
#             return g
#
#
# def cache_gcd(f):
#     cache = {}
#
#     @wraps(f)
#     def wrapped(a, b):
#         key = (a, b)
#         try:
#             result = cache[key]
#         except KeyError:
#             result = cache[key] = f(a, b)
#         return result
#     return wrapped
