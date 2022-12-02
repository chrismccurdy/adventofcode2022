from enum import Enum
from functools import reduce
import operator
import sys


class Play(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3


class GameResults(Enum):
    Loss = 0
    Win = 6
    Draw = 3


opponent_play_map = {
    'A': Play.Rock,
    'B': Play.Paper,
    'C': Play.Scissors
}


my_play_map = {
    'X': Play.Rock,
    'Y': Play.Paper,
    'Z': Play.Scissors
}


outcome_map = {
    'X': GameResults.Loss,
    'Y': GameResults.Draw,
    'Z': GameResults.Win
}


def read_input(input: str) -> list[str]:
    file = open(input, 'r')
    return file.readlines()


def get_my_points_for_game(game: str) -> int:
    game_play_list = game.strip().split(' ')
    opponent_play = opponent_play_map[game_play_list[0]]
    my_play = my_play_map[game_play_list[1]]
    game_results = get_my_game_results(opponent_play, my_play)
    return get_total_points(my_play, game_results)


def get_my_points_for_outcome(game: str) -> int:
    game_play_list = game.strip().split(' ')
    opponent_play = opponent_play_map[game_play_list[0]]
    outcome = outcome_map[game_play_list[1]]
    my_play = get_my_play(opponent_play, outcome)
    return get_total_points(my_play, outcome)


def get_my_game_results(opponent_play: Play, my_play: Play) -> GameResults:
    if opponent_play == my_play:
        return GameResults.Draw
    elif (opponent_play.value + 1) % 3 == my_play.value % 3:
        return GameResults.Win
    else:
        return GameResults.Loss


def get_my_play(opponent_play: Play, outcome: GameResults) -> Play:
    match outcome:
        case GameResults.Draw:
            return opponent_play
        case GameResults.Win:
            return Play(opponent_play.value % 3 + 1)
        case GameResults.Loss:
            return Play((opponent_play.value - 2) % 3 + 1)


def get_total_points(my_play: Play, game_results: GameResults) -> int:
    return my_play.value + game_results.value


def do_both_operations(game: str) -> tuple[int]:
    return (
        get_my_points_for_game(game),
        get_my_points_for_outcome(game)
    )


if __name__ == '__main__':
    total_points = reduce(
        lambda x, y: tuple(map(operator.add, x, y)),
        map(
            do_both_operations,
            read_input(sys.argv[1])
        )
    )
    print(f'[{total_points}]')
