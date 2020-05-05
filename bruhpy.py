import pygame
import maingg
from InputBox import InputBox
from random import randint, choice
import sqlite3
from time import sleep

pygame.init()

conn = sqlite3.connect("data.db")
c = conn.cursor()

try:
    c.execute("CREATE TABLE players (name text, score int)")
except sqlite3.OperationalError:
    pass

field_ize = 30
line_size = 1


red_field = pygame.Surface((field_ize, field_ize))
red_field.fill((170, 50, 50))

grey_field = pygame.Surface((field_ize, field_ize))
grey_field.fill((200, 200, 200))

screen = pygame.display.set_mode((200+(field_ize*20)+(line_size*24), (field_ize*10)+(line_size*12)+100))

background = pygame.image.load("menu_background.png")


class Menu():
    def __init__(self, screen):
        self.screen = screen
        global background
        self.background = background
        self.screen.blit(self.background, (0, 0))

        self.font = pygame.font.Font(None, 58)

        self.create_server_text = self.font.render("CREATE SERVER", True, (50, 50, 50))
        self.create_server_rect = pygame.Rect(10, 74, 350, 40)

        self.connect_text = self.font.render("CONNECT", True, (50, 50, 50))
        self.connect_rect = pygame.Rect(10, 138, 195, 40)

        self.botgame_text = self.font.render("BOT", True, (50, 50, 50))
        self.botgame_rect = pygame.Rect(10, 10, 90, 40)

        self.score_text = self.font.render("SCORE", True, (50, 50, 50))
        self.score_rect = pygame.Rect(10, 202, 140, 40)

        self.screen.blit(self.create_server_text, self.create_server_rect)
        self.screen.blit(self.connect_text, self.connect_rect)
        self.screen.blit(self.botgame_text, self.botgame_rect)
        self.screen.blit(self.score_text, self.score_rect)

        pygame.display.update()

    def menu(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.create_server_rect.collidepoint(event.pos):
                        #создание лобби
                        pass
                    elif self.connect_rect.collidepoint(event.pos):
                        self.screen.blit(self.background, (0,0))
                        connect_window = ConnectWindow(self.screen)
                        if connect_window.window() == -5:
                            return -5
                    elif self.botgame_rect.collidepoint(event.pos):
                        bot_menu = BotMenu(self.screen)
                        if bot_menu.menu() == -5:
                            return -5
                    elif self.score_rect.collidepoint(event.pos):
                        score = ScoreTable(self.screen)
                        if score.score() == -5:
                            return -5


class ScoreTable():
    def __init__(self, screen):
        self.screen = screen
        self.background = background
        self.screen.blit(self.background, (0,0))

        self.font = pygame.font.Font(None, 35)
        self.name_text = self.font.render("Name", True, (0,0,0))
        self.score_text = self.font.render("Score", True, (0,0,0))
        pygame.draw.aaline(self.screen, (0,0,0), (10, 40), (10, 430))
        pygame.draw.aaline(self.screen, (0,0,0), (360, 40), (360, 430))
        pygame.draw.aaline(self.screen, (0,0,0), (10, 40), (360, 40))
        pygame.draw.aaline(self.screen, (0,0,0), (10, 430), (360, 430))
        pygame.draw.aaline(self.screen, (0, 0, 0), (180, 40), (180, 430))
        self.screen.blit(self.name_text, (35, 5))
        self.screen.blit(self.score_text, (215, 5))
        c.execute("SELECT * FROM players ORDER BY score")
        self.mass = c.fetchall()
        if len(self.mass) >=10:
            self.mass = self.mass[-10:]
        else:
            self.mass = self.mass[-len(self.mass):]
        self.mass.reverse()
        y = 42
        for i in self.mass:
            name = self.font.render(i[0], True, (0,0,0))
            number = self.font.render(str(i[1]),True, (0,0,0))
            self.screen.blit(name, (12, y))
            self.screen.blit(number, (182, y))
            pygame.draw.aaline(self.screen, (0, 0, 0), (10, y+28), (360, y+28))
            y+=40

        self.exit_text = pygame.font.Font(None, 58).render("TO MENU", True, (0,0,0))
        self.exit_rect = pygame.Rect(365, 390, 200, 40)
        self.screen.blit(self.exit_text, self.exit_rect)
        pygame.display.update()

    def score(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.exit_rect.collidepoint(event.pos):
                        menu = Menu(screen)
                        if menu.menu() == -5:
                            return -5


class ConnectWindow():
    def __init__(self, screen):
        self.screen = screen
        global background
        self.font = pygame.font.Font(None, 29)
        self.background = background

        self.Ip_text = self.font.render("IP", True, (50, 50, 50))
        self.Ip_Box = InputBox(10, 130, 378, 40)

        self.Name_text = self.font.render("Your name:", True, (50, 50, 50))
        self.Name_Box = InputBox(10, 200, 378, 40)
        self.input_boxes = [self.Ip_Box, self.Name_Box]

    def window(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()

            self.screen.blit(self.background, (0,0))
            for box in self.input_boxes:
                box.draw(self.screen)

            self.screen.blit(self.Name_text, (10, 100))
            self.screen.blit(self.Ip_text, (10, 175))
            pygame.display.update()


class HostWindow():
    def __init__(self, screen):
        self.screen = screen
        global background
        self.background = background
        nameBox
        self.players = []


class Game():
    def __init__(self, screen, player2):

        self.screen = screen
        self.screen.fill((150,150,150))

        global red_field, grey_field, line_size, field_ize

        self.field_ize = field_ize
        self.line_size = line_size
        self.rect_size = (self.field_ize*10)+(self.line_size*11)

        self.fieodandline = (field_ize + line_size)

        self.red_field = red_field
        self.grey_field = grey_field

        self.battleship = pygame.image.load("battleship.png")
        self.cruiser = pygame.image.load("cruiser.png")
        self.destroyer = pygame.image.load("destroyer.png")
        self.cutter = pygame.image.load("cutter.png")

        self.green_field = pygame.Surface((field_ize, field_ize))
        self.green_field.fill((50, 150, 50))

        self.ships_fieldRect = pygame.Rect((50, 50, self.rect_size, self.rect_size))
        self.shots_fieldRect = pygame.Rect((150+self.rect_size, 50, self.rect_size, self.rect_size))

        self.ships_fieldSurf = pygame.Surface((self.rect_size, self.rect_size))
        self.shots_fieldSurf = pygame.Surface((self.rect_size, self.rect_size))
        self.ships_fieldSurf.fill((255,255,255))
        self.shots_fieldSurf.fill((255,255,255))
        self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
        self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)



        self.player1 = maingg.Player()
        self.player2 = player2

        pygame.display.update()
        self.move = 1
        self.arrange()

    def game(self):
        while True:
            for event in pygame.event.get():
                y = self.line_size
                for i in self.player1.ships:
                    x = self.line_size
                    for u in i:
                        if u == -1:
                            self.ships_fieldSurf.blit(self.red_field, (x, y))
                        x += self.field_ize + self.line_size
                    y += self.field_ize + self.line_size
                for y in range(12):
                    pygame.draw.aaline(self.ships_fieldSurf, (0,0,0), (0, y*31), (312, y*31))
                    pygame.draw.aaline(self.shots_fieldSurf, (0, 0, 0), (0, y*31), (312, y*31))
                for x in range(12):
                    pygame.draw.aaline(self.ships_fieldSurf, (0,0,0), (x*31, 0), (x*31, 312))
                    pygame.draw.aaline(self.shots_fieldSurf, (0, 0, 0), (x*31, 0), (x*31, 312))

                y = self.line_size
                for i in self.player1.ships_visual:
                    x = self.line_size
                    for u in i:
                        if u == 1:
                            self.ships_fieldSurf.blit(self.cutter, (x, y))
                        elif u == 2:
                            self.ships_fieldSurf.blit(self.destroyer, (x, y - self.field_ize))
                        elif u == 3:
                            self.ships_fieldSurf.blit(self.cruiser, (x, y - (self.field_ize * 2)))
                        elif u == 4:
                            self.ships_fieldSurf.blit(self.battleship, (x, y))
                        elif u == -1:
                            self.ships_fieldSurf.blit(self.red_field, (x, y))
                        x += self.field_ize + self.line_size
                    y += self.field_ize + self.line_size
                if event.type == pygame.QUIT:
                    return -5
                if self.move == 1:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.shots_fieldRect.collidepoint(event.pos):
                            x = int((event.pos[0] - (150+self.rect_size))/self.fieodandline)
                            if x == 10:
                                x -= 1
                            y = int((event.pos[1]-50)/self.fieodandline)
                            if y == 10:
                                y -= 1
                            if self.player1.shots[y][x] == 0:
                                hp, self.player2.ships = self.player1.shoot(x, y, self.player2.ships)
                                self.player2.alive += hp
                                self.move *= -1
                else:
                    hp, self.player1.ships = self.player2.shoot(self.player1.ships)
                    self.player1.alive += hp
                    self.move *= -1

                y = self.line_size
                for i in self.player2.shots:
                    x = self.line_size
                    for u in i:
                        if u == 2:
                            self.ships_fieldSurf.blit(self.green_field, (x, y))
                        x += self.field_ize + self.line_size
                    y += self.field_ize + self.line_size

                y = self.line_size
                for i in self.player1.shots:
                    x = self.line_size
                    for u in i:
                        if u == 1:
                            self.shots_fieldSurf.blit(self.red_field, (x, y))
                        elif u == 2:
                            self.shots_fieldSurf.blit(self.grey_field, (x, y))
                        x += self.field_ize + self.line_size
                    y += self.field_ize + self.line_size

                self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
                self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)
                if self.player1.alive == 0:
                    y = self.line_size
                    for i in self.player1.shots:
                        x = self.line_size
                        for u in i:
                            if u == 1:
                                self.shots_fieldSurf.blit(self.red_field, (x, y))
                            elif u == 2:
                                self.shots_fieldSurf.blit(self.grey_field, (x, y))
                            x += self.field_ize + self.line_size
                        y += self.field_ize + self.line_size
                        pygame.display.update()
                    sleep(5)
                    return "player2"
                elif self.player2.alive == 0:
                    y = self.line_size
                    for i in self.player1.shots:
                        x = self.line_size
                        for u in i:
                            if u == 1:
                                self.shots_fieldSurf.blit(self.red_field, (x, y))
                            elif u == 2:
                                self.shots_fieldSurf.blit(self.grey_field, (x, y))
                            x += self.field_ize + self.line_size
                        y += self.field_ize + self.line_size
                    pygame.display.update()
                    sleep(5)
                    return "player1"
            pygame.display.update()

    def arrange(self):
        font = pygame.font.Font(None, 29)
        a = 4
        while a:
            self.screen.fill((150,150,150))
            text = font.render(f"Place {a} cutters.", True, (0,0,0))
            self.screen.blit(text, (180,10))
            self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
            self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)
            y = self.line_size
            for y in range(12):
                pygame.draw.aaline(self.ships_fieldSurf, (0, 0, 0), (0, y * 31), (312, y * 31))
                pygame.draw.aaline(self.shots_fieldSurf, (0, 0, 0), (0, y * 31), (312, y * 31))
            for x in range(12):
                pygame.draw.aaline(self.ships_fieldSurf, (0, 0, 0), (x * 31, 0), (x * 31, 312))
                pygame.draw.aaline(self.shots_fieldSurf, (0, 0, 0), (x * 31, 0), (x * 31, 312))
            for i in self.player1.ships_visual:
                y = self.line_size
                for i in self.player1.ships_visual:
                    x = self.line_size
                    for u in i:
                        if u == 1:
                            self.ships_fieldSurf.blit(self.cutter, (x, y))
                        elif u == 2:
                            self.ships_fieldSurf.blit(self.destroyer, (x, y - self.field_ize))
                        elif u == 3:
                            self.ships_fieldSurf.blit(self.cruiser, (x, y - (self.field_ize * 2)))
                        elif u == 4:
                            self.ships_fieldSurf.blit(self.battleship, (x, y))
                        elif u == -1:
                            self.ships_fieldSurf.blit(self.red_field, (x, y))
                        x += self.field_ize + self.line_size
                    y += self.field_ize + self.line_size
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ships_fieldRect.collidepoint(event.pos):
                        x = int((event.pos[0] - 50) / self.fieodandline)
                        if x == 10:
                            x -= 1
                        y = int((event.pos[1] - 50) / self.fieodandline)
                        if y == 10:
                            y -= 1
                        if self.player1.ships[y][x] == 0:
                            self.player1.ships[y][x] = 1
                            self.player1.ships_visual[y][x] = 1
                            a -= 1
            mouse_pos = pygame.mouse.get_pos()
            self.screen.blit(self.cutter, (int(mouse_pos[0]-(self.field_ize/2)), int(mouse_pos[1]-(self.field_ize/2))))
            pygame.display.update()
        a = 3
        while a:
            self.screen.fill((150, 150, 150))
            text = font.render(f"Place {a} destroyers.", True, (0, 0, 0))
            self.screen.blit(text, (180, 10))
            self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
            self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)
            y = self.line_size
            for i in self.player1.ships_visual:
                x = self.line_size
                for u in i:
                    if u == 1:
                        self.ships_fieldSurf.blit(self.cutter, (x, y))
                    elif u == 2:
                        self.ships_fieldSurf.blit(self.destroyer, (x, y - self.field_ize))
                    elif u == 3:
                        self.ships_fieldSurf.blit(self.cruiser, (x, y - (self.field_ize * 2)))
                    elif u == 4:
                        self.ships_fieldSurf.blit(self.battleship, (x, y))
                    x += self.field_ize + self.line_size
                y += self.field_ize + self.line_size
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ships_fieldRect.collidepoint(event.pos):
                        x = int((event.pos[0] - 50) / self.fieodandline)
                        if x == 10:
                            x -= 1
                        y = int((event.pos[1] - 50) / self.fieodandline)
                        if y == 10:
                            y -= 1
                        if y != 0:
                            if self.player1.ships[y][x] == 0 and self.player1.ships[y-1][x] == 0:
                                self.player1.ships[y][x] = 1
                                self.player1.ships_visual[y][x] = 2
                                self.player1.ships[y - 1][x] = 1
                                a -= 1
            mouse_pos = pygame.mouse.get_pos()
            destroyer_ship_mouse = pygame.Rect(
                int(mouse_pos[0] - (self.field_ize / 2)),
                int(mouse_pos[1] - (self.field_ize / 2)-self.field_ize),
                self.field_ize,
                self.field_ize*2)
            self.screen.blit(self.destroyer, destroyer_ship_mouse)
            pygame.display.update()
        a = 2
        while a:
            self.screen.fill((150, 150, 150))
            text = font.render(f"Place {a} cruisers.", True, (0, 0, 0))
            self.screen.blit(text, (180, 10))
            self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
            self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)
            y = self.line_size
            for i in self.player1.ships_visual:
                x = self.line_size
                for u in i:
                    if u == 1:
                        self.ships_fieldSurf.blit(self.cutter, (x, y))
                    elif u == 2:
                        self.ships_fieldSurf.blit(self.destroyer, (x, y - self.field_ize))
                    elif u == 3:
                        self.ships_fieldSurf.blit(self.cruiser, (x, y - (self.field_ize * 2)))
                    elif u == 4:
                        self.ships_fieldSurf.blit(self.battleship, (x, y))
                    elif u == -1:
                        self.ships_fieldSurf.blit(self.red_field, (x, y))
                    x += self.field_ize + self.line_size
                y += self.field_ize + self.line_size
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ships_fieldRect.collidepoint(event.pos):
                        x = int((event.pos[0] - 50) / self.fieodandline)
                        if x == 10:
                            x -= 1
                        y = int((event.pos[1] - 50) / self.fieodandline)
                        if y == 10:
                            y -= 1
                        if y > 1:
                            if self.player1.ships[y][x] == 0 and self.player1.ships[y-1][x] == 0 and self.player1.ships[y - 2][x] == 0:
                                self.player1.ships[y][x] = 1
                                self.player1.ships_visual[y][x] = 3
                                self.player1.ships[y - 1][x] = 1
                                self.player1.ships[y - 2][x] = 1
                                a -= 1
            mouse_pos = pygame.mouse.get_pos()
            destroyer_ship_mouse = pygame.Rect(
                int(mouse_pos[0] - (self.field_ize / 2)),
                int(mouse_pos[1] - (self.field_ize / 2)-(self.field_ize*2)),
                self.field_ize,
                self.field_ize*3)
            self.screen.blit(self.cruiser, destroyer_ship_mouse)
            pygame.display.update()
        a = 1
        while a:
            self.screen.fill((150, 150, 150))
            text = font.render(f"Place the battleship.", True, (0, 0, 0))
            self.screen.blit(text, (180, 10))
            self.screen.blit(self.ships_fieldSurf, self.ships_fieldRect)
            self.screen.blit(self.shots_fieldSurf, self.shots_fieldRect)
            y = self.line_size
            for i in self.player1.ships_visual:
                x = self.line_size
                for u in i:
                    if u == 1:
                        self.ships_fieldSurf.blit(self.cutter, (x, y))
                    elif u == 2:
                        self.ships_fieldSurf.blit(self.destroyer, (x, y - self.field_ize))
                    elif u == 3:
                        self.ships_fieldSurf.blit(self.cruiser, (x, y - (self.field_ize * 2)))
                    elif u == 4:
                        self.ships_fieldSurf.blit(self.battleship, (x, y))
                    elif u == -1:
                        self.ships_fieldSurf.blit(self.red_field, (x, y))
                    x += self.field_ize + self.line_size
                y += self.field_ize + self.line_size
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.ships_fieldRect.collidepoint(event.pos):
                        x = int((event.pos[0] - 50) / self.fieodandline)
                        if x == 10:
                            x -= 1
                        y = int((event.pos[1] - 50) / self.fieodandline)
                        if y == 10:
                            y -= 1
                        if x < 7:
                            if self.player1.ships[y][x] == 0 and self.player1.ships[y][x+1] == 0 and self.player1.ships[y][x+1] == 0 and self.player1.ships[y][x+3] == 0:
                                self.player1.ships[y][x] = 1
                                self.player1.ships_visual[y][x] = 4
                                self.player1.ships[y][x+1] = 1
                                self.player1.ships[y][x+2] = 1
                                self.player1.ships[y][x+3] = 1
                                a -= 1
            mouse_pos = pygame.mouse.get_pos()
            destroyer_ship_mouse = pygame.Rect(
                int(mouse_pos[0] - (self.field_ize / 2)),
                int(mouse_pos[1] - (self.field_ize / 2)),
                self.field_ize * 4,
                self.field_ize)
            self.screen.blit(self.battleship, destroyer_ship_mouse)
            pygame.display.update()
        self.screen.fill((150,150,150))



class Bot(maingg.Player):
    def __init__(self):
        super().__init__()
        self.alive = 20
        self.can_shoot = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
        self.arrenge()

    def shoot(self, ships):
        try:
            where = choice(self.can_shoot)
        except:
            pass
        x = where%10
        y = where//10
        self.can_shoot.remove(where)
        if ships[y][x] == 1:
            self.shots[y][x] = 1
            ships[y][x] = -1
            return -1, ships
        else:
            self.shots[y][x] = 2
            return 0, ships

    def arrenge(self):
        can_place = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                     27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51,
                     52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76,
                     77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]

        available = [1,1,1,1,2,2,2,3,3,4]

        while available!=[]:
            place = choice(can_place)
            ship = choice(available)
            y = place // 10
            x = place % 10
            if ship == 1:
                can_place.remove(place)
                available.remove(1)
                self.ships[y][x] = 1
                self.ships_visual[y][x] = 1
            elif ship == 2:
                if place//10!=0:
                    if self.ships[y-1][x] == 0:
                        available.remove(2)
                        can_place.remove(place)
                        self.ships[y][x] = 1
                        self.ships[y-1][x] = 1
                        self.ships_visual[y][x] = 2
            elif ship == 3:
                if place//10 > 1:
                    if self.ships[y-1][x] == 0 and self.ships[y-2][x]==0 and self.ships[y][x] == 0:
                        available.remove(3)
                        can_place.remove(place)
                        self.ships[y][x] = 1
                        self.ships[y - 1][x] = 1
                        self.ships[y - 2][x] = 1
                        self.ships_visual[y][x] = 3
            elif ship == 4:
                if (place+3)//10 == place//10:
                    if self.ships[y][x+1] == 0 and self.ships[y - 2][x+2] == 0 and self.ships[y][x] == 0:
                        available.remove(4)
                        can_place.remove(place)
                        self.ships[y][x] = 1
                        self.ships[y][x+1] = 1
                        self.ships[y][x+2] = 1
                        self.ships[y][x+3] = 1
                        self.ships_visual[y][x] = 4


class BotMenu():
    def __init__(self, screem):
        self.screen = screen

        self.font = pygame.font.Font(None, 29)
        self.background = background
        self.Name_text = self.font.render("Your name:", True, (50, 50, 50))
        self.Name_Box = InputBox(10, 200, 378, 40)
        self.bot = Bot()
        self.name = None

    def menu(self):
        if self.name == None:
            text = None
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        return -5
                    text = self.Name_Box.handle_event(event)
                self.Name_Box.update()
                self.screen.blit(self.background, (0,0))
                self.Name_Box.draw(self.screen)
                self.screen.blit(self.Name_text, (10, 100))

                if text != None:
                    self.name = text
                    print(self.name)
                    if self.start_game() == -5:
                        return -5
                pygame.display.update()
        else:
            if self.start_game() == -5:
                return -5

    def start_game(self):
        c.execute("SELECT * FROM players WHERE name=?", [(self.name)])
        player = c.fetchone()
        if player is None:
            c.execute(f"INSERT INTO players VALUES('{self.name}', '0')")
            conn.commit()
            c.execute("SELECT * FROM players WHERE name=?", [(self.name)])
            player = c.fetchone()
        conn.commit()
        bot = Bot()
        game = Game(self.screen, bot)
        result = game.game()
        if result == -5:
            return -5
        if result == "player1":
            c.execute(f"UPDATE players SET score = '{player[1]+1}' WHERE name = '{player[0]}'")
            conn.commit()
            if self.game_over("WIN") == -5:
                return -5
        elif result == "player2":
            c.execute(f"UPDATE players SET score = '{player[1] + 1}' WHERE name = '{player[0]}'")
            conn.commit()
            if self.game_over("LOSE") == -5:
                return -5

    def game_over(self, text):

        self.screen.blit(self.background, (0,0))
        message = self.font.render(f"YOU {text}", True, (50,50,50))
        self.screen.blit(message, (10, 130))

        exit_text = self.font.render("EXIT TO MENU", True, (50,50,50))
        exit_rect = pygame.Rect(10, 380, 140, 20)

        continue_text = self.font.render("CONTINUE", True, (50,50,50))
        continue_rect = pygame.Rect(10, 340, 110, 20)

        self.screen.blit(exit_text, exit_rect)
        self.screen.blit(continue_text, continue_rect)

        pygame.display.update()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return -5
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if exit_rect.collidepoint(event.pos):
                        menu = Menu(self.screen)
                        if menu.menu() == -5:
                            return -5
                    elif continue_rect.collidepoint(event.pos):
                        self.menu()

bot = Bot()
menu = Menu(screen)
try:
    menu.menu()
except:
    pass
