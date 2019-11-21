class GameManager:
    def __init__(self, p1, p2):
        self.player1 = p1
        self.player2 = p2

    def run_round(self):
        print ("BEFORE PLAYER1")
        print (self.player1.make_move())
        print ("AFTER PLAYER1")
        print ("BEFORE PLAYER2")
        print (self.player2.make_move())
        print ("AFTER PLAYER2")

    def run_game(self):
        while (True):
            self.run_round()