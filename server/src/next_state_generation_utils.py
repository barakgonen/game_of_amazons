import copy

from server.src.board_game import BoardGame
from server.src.game_node import GameNode


def generate_possible_board_states_for_amazona(current_game_node,
                                               amazona,
                                               blocking_rocks_manager,
                                               available_steps_manager,
                                               turn_validator):
    """
    :param current_board_game: game_node, representing current game state
    :param amazona: current amazona were working on
    :param blocking_rocks_manager: class calculates number of available options to shoot blocking rock in specific state
    :return: array of possible board states if we move amazona (it's possible movement and throw of blocking rock)
    """
    available_states_for_amazona = []
    available_steps_for_amazona = current_game_node.get_available_steps_for_amazona(amazona)
    for available_move in available_steps_for_amazona:
        players_current_pos = []
        available_throwing_rocks_options = []
        if current_game_node.is_black_player_plays():
            players_current_pos = copy.deepcopy(current_game_node.get_black_amazons())
            players_current_pos.remove(amazona)
            players_current_pos.append(available_move)

            # Creating new board with movement of black player
            next_state_board = BoardGame(current_game_node.get_board_size(),
                                         current_game_node.get_white_amazons(),
                                         players_current_pos,
                                         current_game_node.get_blocking_rocks())
            available_throwing_rocks_options = blocking_rocks_manager. \
                generate_available_throwing_options(next_state_board, available_move)

        else:
            players_current_pos = copy.deepcopy(current_game_node.get_white_amazons())
            players_current_pos.remove(amazona)
            players_current_pos.append(available_move)
            # Creating new board with movement of white player
            next_state_board = BoardGame(current_game_node.get_board_size(),
                                         players_current_pos,
                                         current_game_node.get_black_amazons(),
                                         current_game_node.get_blocking_rocks())
            available_throwing_rocks_options = blocking_rocks_manager. \
                generate_available_throwing_options(next_state_board, available_move)

        # THIS IS THE FUCKING IDEA OF A B PRUNING!!! INSTEAD OF JUST CUTTING AS YOU DID BEFORE!
        for available_throwing_option in available_throwing_rocks_options:
            throwing_option = copy.deepcopy(current_game_node.get_blocking_rocks())
            throwing_option.append(available_throwing_option)
            throwing_option = throwing_option
            if current_game_node.is_black_player_plays():
                next_state_board = BoardGame(current_game_node.get_board_size(),
                                             current_game_node.get_white_amazons(),
                                             players_current_pos,
                                             throwing_option)
            else:
                next_state_board = BoardGame(current_game_node.get_board_size(),
                                             players_current_pos,
                                             current_game_node.get_black_amazons(),
                                             throwing_option)
            turn_game_node = GameNode(next_state_board,
                                      turn_validator,
                                      available_steps_manager,
                                      not current_game_node.is_black_player)
            available_states_for_amazona.append(turn_game_node)
            del throwing_option
            del next_state_board
        del players_current_pos
    return available_states_for_amazona


def generate_possible_states_for_amazona_from_game_node(current_game_node,
                                                        amazona,
                                                        blocking_rocks_manager,
                                                        available_steps_manager,
                                                        turn_validator):
    return generate_possible_board_states_for_amazona(current_game_node,
                                                      amazona,
                                                      blocking_rocks_manager,
                                                      available_steps_manager,
                                                      turn_validator)
