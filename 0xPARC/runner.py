import argparse
import importlib
import logging


def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError('List size mismatch.')
    return sum(i * j for i, j in zip(a, b))


def make_game(secret_list):
    secret = secret_list
    n = len(secret)
    n_operations = 0

    def _oracle(x):
        nonlocal n_operations
        n_operations += 1
        logging.debug(f'Oracle call number: {n_operations}')
        return dot_product(secret, x)

    def _n_operations():
        return n_operations

    class Game:
        __slots__ = ('n',)

        def __init__(self):
            self.n = n

        @property
        def n_operations(self):
            return _n_operations()

        def oracle(self, x):
            return _oracle(x)

    def check(guessed):
        return guessed == secret

    return Game(), check


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument('--secret', required=True, help='Comma-separated ints, e.g. "2,200,400"')
    p.add_argument('--player', default='player', help='Module name (default: player)')
    p.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'],
        help='Logging level (default: INFO)',
    )
    return p.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=getattr(logging, args.log_level))

    secret = [int(s.strip()) for s in args.secret.split(",") if s.strip()]
    player = importlib.import_module(args.player)
    game, check = make_game(secret)
    guessed = player.guess_list(game)

    if check(guessed):
        logging.info('Result matches target.')
        logging.info(f'Discovered secret list {secret} using {game.n_operations} oracle operations.')
        return 0

    logging.info('No match.')
    logging.info(f'Guessed {guessed} instead of {secret} using {game.n_operations} oracle operations ')
    return 1


if __name__ == '__main__':
    raise SystemExit(main())
