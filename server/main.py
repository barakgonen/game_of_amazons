import json
import os
import SimpleHTTPServer
import SocketServer
from player import ComputerPlayer, HumanPlayer
from game_manager import GameManager
from turn_validator import TurnValidator
import requests
from web_socket_adapter import WebSocketAdapter

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

def main():
  # p1 = HumanPlayer("BARAK")
  # p2 = ComputerPlayer("ALGORITHM")
  # turn_validator = TurnValidator("")

  websocket_adapter = WebSocketAdapter('ws://localhost:9900')
  websocket_adapter.send_message("bla bla")

  # manager = GameManager(p1, p2, turn_validator)
  # manager.run_game()

if __name__ == "__main__":
    main()
