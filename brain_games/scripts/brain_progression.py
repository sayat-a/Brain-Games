from brain_games.games import brain_progression
from brain_games import engine


def main():
    engine.start_game(brain_progression, brain_progression.GAME_RULES)


if __name__ == '__main__':
    main()
