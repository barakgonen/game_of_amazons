import websocket
from websocket import create_connection
try:
    import thread
except ImportError:
    import _thread as thread
import time

class WebSocketAdapter():
    def __init__(self, url):
        self.ws = create_connection(url)
    
    def send_message(self, msg):
        self.ws.send(msg)
    
    def on_message(self, ws, message):
        print(message)
        
    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")
    
    def on_open(self, ws):
        def run(*args):
            for i in range(3):
                time.sleep(1)
                ws.send("Hello %d" % i)
                time.sleep(1)
            ws.close()
            print("thread terminating...")
        thread.start_new_thread(run, ())