import pygame
import Boy
import CommandUpdate
import CommandDraw

import CommandUp
import CommandDown
import CommandLeft
import CommandRight
import CommandUpLeft
import CommandUpRight
import CommandDownLeft
import CommandDownRight

import Play


class Game:
    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 720
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    def __init__(self):
        self.SCREEN.fill((255, 255, 255))
        self.player = Boy.Boy(350, 350, self.SCREEN)
        self.CommandUpdate = CommandUpdate.CommandUpdate(self.player)
        self.CommandDraw = CommandDraw.CommandDraw(self.player)

        self.CommandUp = CommandUp.CommandUp(self.player)
        self.CommandDown = CommandDown.CommandDown(self.player)
        self.CommandLeft = CommandLeft.CommandLeft(self.player)
        self.CommandRight = CommandRight.CommandRight(self.player)
        self.CommandDownLeft = CommandDownLeft.CommandDownLeft(self.player)
        self.CommandDownRight = CommandDownRight.CommandDownRight(self.player)
        self.CommandUpLeft = CommandUpLeft.CommandUpLeft(self.player)
        self.CommandUpRight = CommandUpRight.CommandUpRight(self.player)

        self.play = Play.Play()

        # self.invoker_update = Invoker.Invoker(CommandUpdate)
        # self.invoker_draw = Invoker.Invoker(CommandDraw)

    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()

        while run:

            for event in pygame.event.get():
                self.play.set_command(self.CommandUpdate)
                if event.type == pygame.QUIT:
                    run = False
                user_input = pygame.key.get_pressed()
                if user_input[pygame.K_w]:
                    self.play.set_command(self.CommandUp)
                elif user_input[pygame.K_s]:
                    self.play.set_command(self.CommandDown)
                elif user_input[pygame.K_a]:
                    self.play.set_command(self.CommandLeft)
                elif user_input[pygame.K_d]:
                    self.play.set_command(self.CommandRight)
                elif user_input[pygame.K_q]:
                    self.play.set_command(self.CommandUpLeft)
                elif user_input[pygame.K_e]:
                    self.play.set_command(self.CommandUpRight)
                elif user_input[pygame.K_z]:
                    self.play.set_command(self.CommandDownLeft)
                elif user_input[pygame.K_c]:
                    self.play.set_command(self.CommandDownRight)

            self.draw_background()

            clock.tick(30)
            pygame.display.update()

    def draw_background(self):
        self.SCREEN.fill((255, 255, 255))
        self.CommandDraw.execute()

