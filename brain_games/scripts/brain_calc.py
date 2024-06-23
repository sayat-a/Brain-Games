from brain_games.games import brain_calc
from brain_games import engine


def main():
    engine.start_game(brain_calc, brain_calc.GAME_RULES)


if __name__ == '__main__':
    main()
