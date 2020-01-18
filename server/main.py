import os
import json
import requests
import SocketServer
import SimpleHTTPServer

from src.constants import Constants
from src.board_game import BoardGame
from src.game_manager import GameManager
from src.turn_validator import TurnValidator
from src.player import ComputerPlayer, HumanPlayer
from src.web_socket_adapter import WebSocketAdapter
from src.blocking_rocks_manager import BlockingRocksManager

def get_config():
  configurationFile = ""
  f = open('./config.json', "r")
  for line in f:
    configurationFile += line
  f.close()
  return configurationFile

def run_server():
  y = json.loads(get_config())
  PORT = y["server-listening-port"]
  Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
  httpd = SocketServer.TCPServer(("", int(PORT)), Handler)
  print "serving at port", PORT
  httpd.serve_forever()

def get_board_size():
  is_input_valid = False
  while (is_input_valid == False):
    try:
      board_size = int(input("Enter prefered board size: " + str(Constants.LARGE_BOARD_SIZE) + "^2 or: " + str(Constants.SMALL_BOARD_SIZE) + "^2"))
    except Exception:
        print "Your input is invalid.. please try again."
        continue
    if (board_size != Constants.LARGE_BOARD_SIZE and board_size != Constants.SMALL_BOARD_SIZE):
      print "Your input is invalid.. please try again."
    else:
      is_input_valid = True
      return board_size

def main():
  board_size = int(get_board_size())
  board_game = BoardGame(board_size)
  blocking_rocks_manager = BlockingRocksManager(board_size)

  p1 = HumanPlayer("BARAK", "WHITE")
  p2 = ComputerPlayer("ALGORITHM", "BLACK")
  turn_validator = TurnValidator(board_game)

  manager = GameManager(p2, p1, turn_validator, board_game, blocking_rocks_manager)
  manager.run_game()

if __name__ == "__main__":
    main()
