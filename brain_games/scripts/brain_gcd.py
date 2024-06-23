from brain_games.games import brain_gcd
from brain_games import engine


def main():
    engine.start_game(brain_gcd, brain_gcd.GAME_RULES)


if __name__ == '__main__':
    main()
