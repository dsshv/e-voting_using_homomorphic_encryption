import lib.scripts.montgomery_reducer as mr
import lib.scripts.math_functions as mf
import math as math


def all_servers_partial(mod: int, num_of_servers: int, server_keys, cryptograms):
    def partial_decrypt(x_num: int, secret_key: int):
        montgomery_reducer = mr.MontgomeryReducer(mod)
        partial_decrypted_message = montgomery_reducer.montgomery_pow(x_num, secret_key)
        return partial_decrypted_message

    servers_decrypted_w = [[0 for i in range(len(cryptograms))] for i in range(num_of_servers)]
    for i in range(num_of_servers):
        s = server_keys[i].random_num_s
        for j in range(len(cryptograms)):
            x = cryptograms[j][0]
            w_partial = partial_decrypt(x, s)
            servers_decrypted_w[i][j] = w_partial
    print(servers_decrypted_w)
    return servers_decrypted_w


def compute_full_x(mod, matrix: list):
    montgomery_reducer = mr.MontgomeryReducer(mod)

    def multiply_parts(servers_decrypted_w: list):
        multiplication_of_transcripts = []
        for i in range(len(servers_decrypted_w[0])):
            voter_mul_w = 1
            for j in range(len(servers_decrypted_w)):
                voter_mul_w = montgomery_reducer.montgomery_multiply(voter_mul_w, servers_decrypted_w[j][i])
            multiplication_of_transcripts.append(voter_mul_w)
        return multiplication_of_transcripts

    full_x = 1
    multiplied_w = multiply_parts(matrix)
    for i in multiplied_w:
        full_x = montgomery_reducer.montgomery_multiply(full_x, i)

    return full_x


def compute_full_y(mod, cryptograms):
    montgomery_reducer = mr.MontgomeryReducer(mod)
    full_y: int = 1
    for i in range(len(cryptograms)):
        full_y = montgomery_reducer.montgomery_multiply(full_y, cryptograms[i][1])
    return full_y


def compute_votes_sum(mod, full_x: int, full_y: int, prime_g: int):
    reverse_x = mf.gcd_extended(full_x, mod)[1]
    montgomery_reducer = mr.MontgomeryReducer(mod)
    prime_pow_sum = montgomery_reducer.montgomery_multiply(full_y, reverse_x)
    votes_sum = math.log(prime_pow_sum, prime_g)
    return votes_sum

