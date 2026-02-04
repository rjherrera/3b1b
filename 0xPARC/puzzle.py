from math import ceil, log10
import logging

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
        logging.debug(f'Oracle call number: {self.n_operations}')
        return dot_product(self.secret_list, x)

    def guess_list(self):
        x_1 = [1 for i in range(self.n)]
        logging.debug(f'List for operation *sum*: {x_1}')
        question_1 = self.oracle(x_1)
        logging.debug(f'Oracle answer for operation *sum*: {question_1}')

        grade = ceil(log10(question_1))
        x_2 = [10 ** (grade * i) for i in range(self.n)]
        logging.debug(f'List for operation *separate*: {x_2}')
        question_2 = self.oracle(x_2)
        logging.debug(f'Oracle answer for operation *separate*: {question_2}')

        v_candidate = [question_2 % x_2[i + 1] // x_2[i] for i in range(len(x_2) - 1)] + [question_2 // x_2[-1]]
        logging.debug(f'Guessed list: {v_candidate}')
        return v_candidate

    def experiment(self):
        return self.guess_list() == self.secret_list


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    game = Game([2, 200, 400, 10, 20, 14])

    if game.experiment():
        logging.info('Result matches target.')
        logging.info(f'Discovered secret list {game.secret_list} using {game.n_operations} oracle operations.')
    else:
        logging.info('No match.')
        logging.info(f'Secret list was {game.secret_list}.')
