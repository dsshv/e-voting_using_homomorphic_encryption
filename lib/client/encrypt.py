from random import randint
from math import gcd, log
import lib.scripts.montgomery_reducer as mr
import lib.scripts.math_functions as mf


def auto_encrypt(modulus_p: int, primitive_root_g, primitive_root_G, pub_key_y):
    encrypted_vote_matrix = []
    votes_file = open('votes.txt', 'r')
    cryptograms = open('cryptograms.txt', 'w')
    while True:
        count = 1
        line = votes_file.readline()
        if not line:
            break
        current_vote = int(line)
        encrypted_vote = EncryptedMessage(pub_key_y, primitive_root_g, modulus_p, primitive_root_G, current_vote)
        print(f'Session key of voter {count}: {encrypted_vote.session_key_k}')
        encrypted_vote_matrix.append(encrypted_vote.return_encrypted_message())
        cryptograms.write(str(encrypted_vote.return_encrypted_message())+'\n')
        count += 1
    votes_file.close()
    cryptograms.close()
    print(encrypted_vote_matrix)
    return encrypted_vote_matrix


def possible_results(mod, g):
    montgomery_reducer = mr.MontgomeryReducer(mod)
    reversed_g = mf.gcd_extended(g, mod)[1]
    while reversed_g < 0:
        reversed_g += mod
    count_of_voters = sum(1 for line in open('votes.txt', 'r'))
    possible_results_file = open('possible_results_table.txt', 'w')
    min_result = -1 * count_of_voters
    result_matrix = [[0 for i in range(3)] for i in range(count_of_voters + 1)]
    for i in range(len(result_matrix)):
        result_matrix[i][0] = min_result + (i * 2) # votes sum
        if result_matrix[i][0] < 1:
            # print('тут', reversed_g, -1 * int(result_matrix[i][0]))
            primitive_pow_sum = montgomery_reducer.montgomery_pow(reversed_g, -1 * int(result_matrix[i][0]))
            result = log(primitive_pow_sum, g)
            result_matrix[i][1] = result
        else:
            primitive_pow_sum = montgomery_reducer.montgomery_pow(g, int(result_matrix[i][0]))
            result = log(primitive_pow_sum, g)
            result_matrix[i][1] = result
        negative_votes = (count_of_voters - result_matrix[i][0]) / 2
        positive_votes = count_of_voters - negative_votes
        result_matrix[i][2] = f'Проголосовали за: {int(positive_votes)}. Проголосовали против: {int(negative_votes)}'
        possible_results_file.write(str(result_matrix[i])+'\n')
    possible_results_file.close()
    return result_matrix

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

    # message: int

    def __init__(self, y: int, g: int, p: int, primitive_second_G: int, vote: int):
        self.modulus_p = p
        self.primitive_root_g = g
        self.open_key_y = y
        self.second_primitive_root_G = primitive_second_G
        self.vote = vote

        self.session_key_k = EncryptedMessage.generate_session_key(self.modulus_p)
        self.montgomery_reducer = mr.MontgomeryReducer(self.modulus_p)

        # self.second_primitive_root_G = randint(1, self.modulus_p - 1)
        # while gcd(self.second_primitive_root_G, self.modulus_p - 1) != 0:
        #     self.second_primitive_root_G = randint(1, self.modulus_p - 1)
        self.first_part_cipher_text_a = self.montgomery_reducer.montgomery_pow(
            self.primitive_root_g, self.session_key_k
        )
        if self.vote < 0:
            reverse_G: int = mf.gcd_extended(self.second_primitive_root_G, self.modulus_p)[1]
            self.second_part_cipher_text_b = self.montgomery_reducer.montgomery_multiply(
                self.montgomery_reducer.montgomery_pow(self.open_key_y, self.session_key_k),
                reverse_G
            )
        else:
            self.second_part_cipher_text_b = self.montgomery_reducer.montgomery_multiply(
                self.montgomery_reducer.montgomery_pow(self.open_key_y, self.session_key_k),
                self.second_primitive_root_G
            )
        # self.message = 10**(self.candidate_id - 1)

    def return_encrypted_message(self):
        return [self.first_part_cipher_text_a, self.second_part_cipher_text_b]

    @staticmethod
    def generate_session_key(p: int):
        k: int = randint(1, p - 1)
        while gcd(k, p - 1) != 1:
            k = randint(1, p - 1)
        return k
