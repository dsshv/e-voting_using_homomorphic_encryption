import math


class MontgomeryReducer:
    modulus: int
    reducer_bits: int
    reducer: int
    mask: int
    reciprocal: int
    factor: int
    convert_done: int

    def __init__(self, mod: int):
        # Modulus
        if mod < 3 or mod % 2 == 0:
            raise ValueError("Modulus must be an odd number at least 3")
        self.modulus = mod

        # Reducer
        self.reducer_bits = (mod.bit_length() // 8 + 1) * 8  # This is a multiple of 8
        self.reducer = 1 << self.reducer_bits  # This is a power of 256
        self.mask = self.reducer - 1
        assert (self.reducer > mod) and (math.gcd(self.reducer, mod) == 1)

        # Other computed numbers
        self.reciprocal = MontgomeryReducer.reciprocal_mod(self.reducer % mod, mod)
        self.factor = (self.reducer * self.reciprocal - 1) // mod
        self.convert_done = self.reducer % mod

    # The range of x is unlimited
    def convert_in(self, x: int) -> int:
        return (x << self.reducer_bits) % self.modulus

    # The range of x is unlimited
    def convert_out(self, x: int) -> int:
        return (x * self.reciprocal) % self.modulus

    # Inputs and output are in Montgomery form and in the range [0, modulus)
    def multiply_algorithm(self, x: int, y: int) -> int:
        mod: int = self.modulus
        assert (0 <= x < mod) and (0 <= y < mod)
        product: int = x * y
        temp: int = ((product & self.mask) * self.factor) & self.mask
        reduced: int = (product + temp * mod) >> self.reducer_bits
        result: int = reduced if (reduced < mod) else (reduced - mod)
        assert 0 <= result < mod
        return result

    # Input x (base) and output (power) are in Montgomery form and in the range [0, modulus); input y (exponent) is
    # in standard form
    def pow_algorithm(self, x: int, y: int) -> int:
        assert 0 <= x < self.modulus
        if y < 0:
            raise ValueError("Negative exponent")
        z: int = self.convert_done
        while y != 0:
            if y & 1 != 0:
                z = self.multiply_algorithm(z, x)
            x = self.multiply_algorithm(x, x)
            y >>= 1
        return z

    @staticmethod
    def reciprocal_mod(x: int, mod: int) -> int:
        # Based on a simplification of the extended Euclidean algorithm
        assert 0 <= x < mod
        y: int = x
        x = mod
        a: int = 0
        b: int = 1
        while y != 0:
            a, b = b, a - x // y * b
            x, y = y, x % y
        if x == 1:
            return a % mod
        else:
            raise ValueError("Reciprocal does not exist")

    def montgomery_multiply(self, x: int, y: int) -> int:
        x = self.convert_in(x)
        y = self.convert_in(y)
        result = self.convert_out(self.multiply_algorithm(x, y))
        return result

    def montgomery_pow(self, x: int, y: int):
        x = self.convert_in(x)
        result = self.convert_out(self.pow_algorithm(x, y))
        return result
