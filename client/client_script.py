import lib.scripts.montgomery_reducer as mr
import lib.scripts.math_functions as mf
from random import randint
from math import gcd


class EncryptedMessage:
    modulus_p: int
    primitive_root_g: int
    open_key_y: int

    vote: int

    session_key_k: int
    montgomery_reducer: mr.MontgomeryReducer
    second_primitive_root_G: int

    first_part_cipher_text_a: int
    second_part_cipher_text_b: int

    def __init__(self, y: int, g: int, p: int, checker_g: int, vote: int):
        self.modulus_p = p
        self.primitive_root_g = g
        self.open_key_y = y
        self.second_primitive_root_G = checker_g
        self.vote = vote

        self.session_key_k = EncryptedMessage.generate_session_key(self.modulus_p)
        self.montgomery_reducer = mr.MontgomeryReducer(self.modulus_p)

        self.first_part_cipher_text_a = self.montgomery_reducer.montgomery_pow(
            self.primitive_root_g, self.session_key_k
        )
        if self.vote < 0:
            checker_g: int = mf.gcd_extended(self.second_primitive_root_G, self.modulus_p)[1]
            self.second_part_cipher_text_b = self.montgomery_reducer.montgomery_multiply(
                self.montgomery_reducer.montgomery_pow(self.open_key_y, self.session_key_k),
                checker_g
            )
        else:
            self.second_part_cipher_text_b = self.montgomery_reducer.montgomery_multiply(
                self.montgomery_reducer.montgomery_pow(self.open_key_y, self.session_key_k),
                self.second_primitive_root_G
            )

    def return_encrypted_message(self):
        return [self.first_part_cipher_text_a, self.second_part_cipher_text_b]

    @staticmethod
    def generate_session_key(p: int):
        k: int = randint(1, p - 1)
        while gcd(k, p - 1) != 1:
            k = randint(1, p - 1)
        return k


def general_open_key(server_keys: list, mod: int):
    general_pub_key_h: int = 1
    montgomery_reducer = mr.MontgomeryReducer(mod)
    for i in range(len(server_keys)):
        if int(server_keys[i][2]) != mod:
            print(server_keys[i][2])
            return 'Unexpected Error: prime p must be same for whole system'
        general_pub_key_h = montgomery_reducer.montgomery_multiply(general_pub_key_h, int(server_keys[i][0]))
    return general_pub_key_h


def got_keys(f: str):
    open_keys = open(f, 'r')
    keys_lines = []
    while True:
        line = open_keys.readline()
        if not line:
            break
        keys_lines.append(line[:-2])
    keys = [i.strip('[]').split(', ') for i in keys_lines]
    print(f'keys is: {str(keys)}')
    return keys
