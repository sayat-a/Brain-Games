from brain_games.games import brain_even
from brain_games import engine


def main():
    engine.start_game(brain_even, brain_even.GAME_RULES)


if __name__ == '__main__':
    main()
