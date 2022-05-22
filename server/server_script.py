import sys
import lib.scripts.montgomery_reducer as mr
import interfaces.server_ui as server_ui
from random import randint

secret_keys_stack = []


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

    def send_open_keys(self):
        global secret_keys_stack
        open_keys = open('open_keys.txt', 'a')
        open_keys.write(str(self.return_key()) + '\n')
        secret_keys_stack.append(str(self.random_num_s))
        open_keys.close()
        return self.return_key()


def init_server_key(prime: int, primitive: int):
    open_keys = open('open_keys.txt', 'r')
    count = 0
    while True:
        line = open_keys.readline()
        if not line:
            break
        count += 1
    key = Key(prime, primitive, count)
    open_keys.close()
    return key


def send_close_keys():
    secret_keys = open('secret_keys.txt', 'w')
    for i in secret_keys_stack:
        secret_keys.write(str(i) + '\n')
    print('secret keys successful wrote\n')


def server_main():
    open_keys = open('open_keys.txt', 'w')
    open_keys.close()
    app = server_ui.QtWidgets.QApplication(sys.argv)
    main_window = server_ui.QtWidgets.QMainWindow()
    ui = server_ui.Ui_Evote_server()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())


def all_servers_partial(mod: int):
    def partial_decrypt(x_num: int, secret_key: int):
        montgomery_reducer = mr.MontgomeryReducer(mod)
        partial_decrypted_message = montgomery_reducer.montgomery_pow(x_num, secret_key)
        return partial_decrypted_message

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

    num_of_servers = len(secret_keys_stack)
    cryptograms = get_cryptograms()
    servers_decrypted_w = [[0 for i in range(len(cryptograms))] for i in range(num_of_servers)]
    for i in range(num_of_servers):
        s = secret_keys_stack[i]
        for j in range(len(cryptograms)):
            x = int(cryptograms[j][0])
            w_partial = partial_decrypt(int(x), int(s))
            servers_decrypted_w[i][j] = w_partial

    print(servers_decrypted_w)
    parts_file = open('cryptograms_parts.txt', 'w')
    for i in range(len(servers_decrypted_w)):
        parts_file.write(f'server №{str(i + 1)} parts:\n')
        parts_file.write(str(servers_decrypted_w[i])+'\n')

    return servers_decrypted_w
