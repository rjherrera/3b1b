from math import ceil, log10

def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError('List size mismatch.')

    return sum(i * j for i, j in zip(a, b))

class Game:
    def __init__(self, secret_list):
        self.secret_list = secret_list
        self.n = len(secret_list)
        self.n_operations = 0

    def oracle(self, x):
        self.n_operations += 1
        return dot_product(self.secret_list, x)

    def guess_list(self):
        x_1 = [1 for i in range(self.n)]
        question_1 = self.oracle(x_1)

        grade = ceil(log10(question_1))
        x_2 = [10 ** (grade * i) for i in range(self.n)]
        question_2 = self.oracle(x_2)

        v_candidate = [question_2 % x_2[i + 1] // x_2[i] for i in range(len(x_2) - 1)] + [question_2 // x_2[-1]]
        return v_candidate

    def experiment(self):
        return self.guess_list() == self.secret_list


if __name__ == '__main__':
    game = Game([2, 200, 400, 10, 20, 14])

    if game.experiment():
        print('Result matches target.')
        print(f'Discovered secret list {game.secret_list} using {game.n_operations} oracle operations.')
    else:
        print('No match.')
        print(f'Secret list was {game.secret_list}.')
