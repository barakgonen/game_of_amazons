import copy

from server.src.game_node import GameNode


def generate_possible_board_states_for_amazona(board_size,
                                               amazona,
                                               player_color,
                                               current_white_amazons,
                                               current_black_amazons,
                                               current_blocking_rocks_pos,
                                               available_steps_manager,
                                               blocking_rocks_manager,
                                               turn_validator):
    """
    :param board_size: size of the board were playing on
    :param amazona: current amazona were working on
    :param player_color: color of playing player
    :param current_white_amazons: current pos of white amazons
    :param current_black_amazons: current pos of black amazons
    :param current_blocking_rocks_pos: current pos of blocking rocks
    :param available_steps_manager: class calculates number of available steps for amazona in specific state
    :param blocking_rocks_manager: class calculates number of available options to shoot blocking rock in specific state
    :param turn_validator: class which handles moevment validation to determinate if possible state is a valid one
    :return: array of possible board states if we move amazona (it's possible movement and throw of blocking rock)
    """
    available_states_for_amazona = []
    available_steps_for_amazona = available_steps_manager.get_available_moves_for_amazona(board_size,
                                                                                          current_white_amazons,
                                                                                          current_black_amazons,
                                                                                          current_blocking_rocks_pos,
                                                                                          player_color,
                                                                                          amazona)
    for available_move in available_steps_for_amazona:
        players_current_pos = []
        available_throwing_rocks_options = []
        if player_color == "BLACK":
            players_current_pos = copy.deepcopy(current_black_amazons)
            players_current_pos.remove(amazona)
            players_current_pos.append(available_move)
            available_throwing_rocks_options = blocking_rocks_manager.generate_available_throwing_options(
                board_size, current_white_amazons, players_current_pos, current_blocking_rocks_pos,
                available_move)
        elif player_color == "WHITE":
            players_current_pos = copy.deepcopy(current_white_amazons)
            players_current_pos.remove(amazona)
            players_current_pos.append(available_move)
            available_throwing_rocks_options = blocking_rocks_manager.generate_available_throwing_options(
                board_size, players_current_pos, current_black_amazons, current_blocking_rocks_pos,
                available_move)
        else:
            raise ValueError("Invalid player color")
        # THIS IS THE FUCKING IDEA OF A B PRUNING!!! INSTEAD OF JUST CUTTING AS YOU DID BEFORE!
        for available_throwing_option in available_throwing_rocks_options:
            throwing_option = copy.deepcopy(current_blocking_rocks_pos)
            throwing_option.append(available_throwing_option)
            if player_color == "BLACK":
                turn_game_node = GameNode(board_size,
                                          turn_validator,
                                          current_white_amazons,
                                          players_current_pos,
                                          throwing_option,
                                          available_steps_manager,
                                          True)
            elif player_color == "WHITE":
                turn_game_node = GameNode(board_size,
                                          turn_validator,
                                          players_current_pos,
                                          current_black_amazons,
                                          throwing_option,
                                          available_steps_manager,
                                          False)
            available_states_for_amazona.append(turn_game_node)
            del throwing_option
        del players_current_pos
    return available_states_for_amazona


def generate_possible_states_for_amazona_from_game_node(current_game_node, amazona_to_move, player_color,
                                                        blocking_rocks_manager):
    return generate_possible_board_states_for_amazona(current_game_node.board_size,
                                                      amazona_to_move,
                                                      player_color,
                                                      current_game_node.white_amazons_pos,
                                                      current_game_node.black_amazons_pos,
                                                      current_game_node.blocking_lst,
                                                      current_game_node.available_steps_manager,
                                                      blocking_rocks_manager,
                                                      current_game_node.turn_validator)
