from random import randint
from math import gcd
import lib.scripts.montgomery_reducer as mr


def init_servers_keys(num_of_servers: int, mod: int, prime: int):
    servers_keys = []
    for i in range(num_of_servers):
        new_server_key = Key(mod=mod, prim=prime, ser_id=(i + 1))
        print(f'Инициализирован Сервер №{new_server_key.return_server_id()}.'
              f' Открытый ключ сервера:{new_server_key.return_key()}. Закрытый ключ: {new_server_key.random_num_s}')
        servers_keys.append(new_server_key)
    return servers_keys


def print_servers_keys(keys):
    server_keys_output_file = open('each_server_key.txt', 'w')
    for i in range(len(keys)):
        server_keys_output_file.write(f'{i + 1}: {keys[i].return_key()}\n')
    server_keys_output_file.close()


def general_open_key(server_keys, mod):
    general_pub_key_h: int = 1
    montgomery_reducer = mr.MontgomeryReducer(mod)
    for i in range(len(server_keys)):
        general_pub_key_h = montgomery_reducer.montgomery_multiply(general_pub_key_h, server_keys[i].computed_key_y)

    return general_pub_key_h


def print_general_open_key(pubkey):
    general_pubkey_output_file = open(' general_pubkey.txt', 'w')
    general_pubkey_output_file.write(f'General public key h is: {pubkey}')
    general_pubkey_output_file.close()


class Key:
    modulus_p: int
    primitive_root_g: int
    random_num_s: int
    server_id: int
    computed_key_y: int

    def __init__(self, mod: int, prim: int, ser_id: int):
        self.modulus_p = mod
        self.primitive_root_g = prim
        self.server_id = ser_id
        self.random_num_s = randint(1, self.modulus_p - 1)
        self.computed_key_y = self.compute_open_key()

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def compute_open_key(self):
        montgomery_reducer: mr.MontgomeryReducer = mr.MontgomeryReducer(self.modulus_p)
        y = montgomery_reducer.montgomery_pow(self.primitive_root_g, self.random_num_s)
        return y

    def return_server_id(self) -> int:
        return self.server_id

    def return_key(self):
        return [self.computed_key_y, self.primitive_root_g, self.modulus_p]
