import random

class cube:
    def __init__(self, color, conn):
        self.color = color
        conn = []
    def add(self, cube):
        self.conn.append(cube)

def rand_color():
    colors = ['w', 'b', 'y', 'g', 'o', 'y']
    return colors[random.randint(len(colors))]

#Start from top left corner, work across and down
def generate_cube():
     curr = 1
     while curr < 26:
         