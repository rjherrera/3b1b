from math import ceil, log10
import logging

def guess_list(game):
    x_1 = [1 for _ in range(game.n)]
    logging.debug(f'List for operation *sum*: {x_1}')
    question_1 = game.oracle(x_1)
    logging.debug(f'Oracle answer for operation *sum*: {question_1}')

    grade = ceil(log10(question_1))
    x_2 = [10 ** (grade * i) for i in range(game.n)]
    logging.debug(f'List for operation *separate*: {x_2}')
    question_2 = game.oracle(x_2)
    logging.debug(f'Oracle answer for operation *separate*: {question_2}')

    v_candidate = [question_2 % x_2[i + 1] // x_2[i] for i in range(len(x_2) - 1)] + [question_2 // x_2[-1]]
    logging.debug(f'Guessed list: {v_candidate}')
    return v_candidate
