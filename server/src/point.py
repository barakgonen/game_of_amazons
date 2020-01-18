class Point:
    """ Point class represents and manipulates x,y coords. represents a position on the board"""

    def __init__(self, x, y):
        """ Create a new point at the origin """
        self.x = str(x).upper()
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
    
    def to_string(self):
        return "<" + str(self.x) + ", " + str(self.y) +">"