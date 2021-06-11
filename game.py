from const import *


class Board(object):
    def __init__(self, player_count = 4):
        self.player_count = player_count




class Field(object):
    def __init__(self, style = None):   #как называть переменную тип если type занят?(
        if not style:
            self.type = 0
        else:
            self.type = style

   
