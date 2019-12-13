import json
import os
import SimpleHTTPServer
import SocketServer
from player import ComputerPlayer, HumanPlayer
from game_manager import GameManager
from turn_validator import TurnValidator
import requests
from web_socket_adapter import WebSocketAdapter
from board_game import BoardGame
from blocking_rocks_manager import BlockingRocksManager
from constants import LARGE_BOARD_SIZE, SMALL_BOARD_SIZE 

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
      board_size = int(input("Enter prefered board size: " + str(LARGE_BOARD_SIZE) + "^2 or: " + str(SMALL_BOARD_SIZE) + "^2"))
    except Exception:
        print "Your input is invalid.. please try again."
        continue
    if (board_size != LARGE_BOARD_SIZE and board_size != SMALL_BOARD_SIZE):
      print "Your input is invalid.. please try again."
    else:
      is_input_valid = True
      return board_size

def main():
  board_size = int(get_board_size())
  board_game = BoardGame(board_size)
  blocking_rocks_manager = BlockingRocksManager(board_size)

  p1 = HumanPlayer("BARAK")
  p2 = ComputerPlayer("ALGORITHM")
  turn_validator = TurnValidator()

  manager = GameManager(p1, p2, turn_validator, board_game, blocking_rocks_manager)
  manager.run_game()

if __name__ == "__main__":
    main()
