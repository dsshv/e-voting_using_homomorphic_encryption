import lib.scripts.montgomery_reducer as mr
import lib.scripts.math_functions as mf
from math import log


def get_parts():
    parts_lines = []
    parts = open('cryptograms_parts.txt', 'r')
    while True:
        line = parts.readline()
        line = parts.readline()
        if not line:
            break
        parts_lines.append(line[:-2])
    parts_matrix = [i.strip('[]').split(', ') for i in parts_lines]
    print(parts_matrix)
    print('done')
    return parts_matrix


def compute_full_x(mod, matrix: list):
    montgomery_reducer = mr.MontgomeryReducer(mod)

    def multiply_parts(servers_decrypted_w: list):
        multiplication_of_transcripts = []
        for i in range(len(servers_decrypted_w[0])):
            voter_mul_w = 1
            for j in range(len(servers_decrypted_w)):
                voter_mul_w = montgomery_reducer.montgomery_multiply(voter_mul_w, int(servers_decrypted_w[j][i]))
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
        full_y = montgomery_reducer.montgomery_multiply(full_y, int(cryptograms[i][1]))
    return full_y


def compute_votes_sum(mod, full_x: int, full_y: int, prime_g: int):
    reverse_x = mf.gcd_extended(full_x, mod)[1]
    montgomery_reducer = mr.MontgomeryReducer(mod)
    prime_pow_sum = montgomery_reducer.montgomery_multiply(full_y, reverse_x)
    votes_sum = log(prime_pow_sum, prime_g)
    return votes_sum


def get_cryptograms():
    cryptograms_txt = open('cryptograms.txt', 'r')
    cryptograms_lines = []
    while True:
        line = cryptograms_txt.readline()
        if not line:
            break
        cryptograms_lines.append(line[:-2])
    text_to_cryptograms = [i.strip('[]').split(', ') for i in cryptograms_lines]
    print(f'cryptograms is: {str(text_to_cryptograms)}')
    return text_to_cryptograms


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
        result_matrix[i][0] = min_result + (i * 2)  # votes sum
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
        possible_results_file.write(str(result_matrix[i]) + '\n')
    possible_results_file.close()
    return result_matrix
