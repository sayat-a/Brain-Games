from brain_games.games import brain_prime
from brain_games import engine


def main():
    engine.start_game(brain_prime, brain_prime.GAME_RULES)


if __name__ == '__main__':
    main()
