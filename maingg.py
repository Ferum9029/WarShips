import pygame


class Player():
    def __init__(self):
        self.ships = [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]]
        self.shots = [[0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0,0,0,0]]
        self.alive = 0

    def add_ship(self, x, y):
        self.ships[y][x] = 1

    def damage(self, x, y):
        if self.ships[y][x] == 1:
            self.ship[y][x] = -1

    def shoot(self,x, y, ships):
        if ships[y][x] == 1:
            self.shots[y][x] = 1
            ships[y][x] = -1
            return -1, ships
        else:
            self.shots[y][x] = 2
            return 0, ships

"""
player1 = Player()
player1.alive = 10
player2 = Player()
player2.alive = 10
while True:
    for i in player1.ships:
        for u in i:
            if u == 1:
                print("@", end=" ")
            if u == -1:
                print("#", end=" ")
            if u == 0:
                print("Ж", end=" ")
        print("\n")
    print("-------------------------------------------------------------------")

    for i in player1.shots:
        for u in i:
            print(u, end=" ")
        print("\n")
    x = int(input("X выстрела(отсчет с нуля)"))
    y = int(input("y выстрела(отсчет с нуля)"))
    player1.shoot(x,y, player2)
    if player1.alive == 0:
        print("player 2 won")
        break
    elif player2.alive == 0:
        print("player 1 won")
        break"""