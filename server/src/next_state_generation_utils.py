
from server.src.board_game import BoardGame
from server.src.game_node import GameNode

def generate_possible_board_states_for_amazona(game_size,
                                               current_game_node,
                                               amazona_to_move,
                                               possible_moves_of_it,
                                               blocking_rocks_manager,
                                               available_steps_manager):
    """
    :param current_game_node: game_node, representing current game state
    :param amazona: current amazona were working on
    :param blocking_rocks_manager: class calculates number of available options to shoot blocking rock in specific state
    :param available_steps_manager:
    :return: array of possible board states if we move amazona (it's possible movement and throw of blocking rock)
    """
    available_states_for_amazona = []
    is_board_ok = True
    is_blocking_rock_ok = True
    for available_move in possible_moves_of_it:
        is_board_ok = current_game_node.current_board.preform_temporary_movement_for_amazon(amazona_to_move, available_move)
        available_throwing_rocks_options = blocking_rocks_manager. \
            generate_available_throwing_options(current_game_node.current_board, available_move)

        for available_throwing_option in available_throwing_rocks_options:
            is_blocking_rock_ok = current_game_node.current_board.preform_temporary_block(available_throwing_option)
            # In order to prevent some board creations, ill modify the board, copy it to new game state and undo change
            if current_game_node.is_black_player_plays():
                turn_game_node = GameNode(current_game_node.current_board,
                                          current_game_node.is_black_player_plays(),
                                          available_steps_manager)

            else:
                turn_game_node = GameNode(current_game_node.current_board,
                                          not current_game_node.is_black_player_plays(),
                                          available_steps_manager)
            available_states_for_amazona.append(turn_game_node)
            current_game_node.current_board.undo_temporary_block(available_throwing_option)
        is_board_ok = current_game_node.current_board.undo_temporary_movement_for_amazon(amazona_to_move, available_move)
    return available_states_for_amazona