import SimpleHTTPServer
import SocketServer
import json

import os
print os.getcwd()

configurationFile = ""
f = open('./config.json', "r")
for line in f:
  configurationFile += line
f.close()

y = json.loads(configurationFile)

PORT = y["server-listening-port"]

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", int(PORT)), Handler)

print "serving at port", PORT
httpd.serve_forever()