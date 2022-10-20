import pygame
from pygame.locals import *
import random
import time
from logic import *

fps = 60
earnings = 10
speed = 2.5
direction_time = (30 / speed) * 4

pygame.init()


def level_screen(level_l):
    y = 0
    for line in level_l:
        x = 0
        for detail in line:
            if detail == 0 or detail == 2 or detail == 3 or detail == 4:
                window.blit(rect_noir, (x, y))
            if detail == "v":
                window.blit(rect_noir, (x, y))
            if detail == 1:
                window.blit(rect_viollet, (x, y))
            x += 30
        y += 30


def level_screen_tablet(level_l):
    y = 15
    for line in level_l:
        x = 15
        for detail in line:
            if detail == 2:
                pygame.draw.circle(window, (255, 255, 255), (x, y), 4)
            x += 30
        y += 30


def level_display():
    level_screen(level_list)
    level_screen_tablet(level_list)
    window.blit(text_title_object, (60, 30))



"""window initialization"""

window = pygame.display.set_mode((690, 900))
pygame.display.set_caption("Pac-man")

"""image initialization"""


image_menu = pygame.image.load("./assets/menu.png").convert()
level_suivant_image = pygame.image.load("./assets/level_suivant.png").convert()
option_image = pygame.image.load("./assets/option.png").convert()
valide_option_image = pygame.image.load("./assets/fantomme_bleu.png").convert_alpha()
game_over_image = pygame.image.load("./assets/gameover.png").convert()
rect_noir = pygame.image.load("./assets/rectangle_noir.png").convert()
rect_viollet = pygame.image.load("./assets/rectangle_viollet.png").convert()
pac_man = pygame.image.load("./assets/pac_man.png").convert_alpha()
fan_bleu = pygame.image.load("./assets/fantomme_bleu.png").convert_alpha()
fan_jaune = pygame.image.load("./assets/fantomme_jaune.png").convert_alpha()
fan_rose = pygame.image.load("./assets/fantomme_rose.png").convert_alpha()
fan_rouge = pygame.image.load("./assets/fantomme_rouge.png").convert_alpha()

"""text initialization"""
text_title = pygame.font.Font(None, 60)
points_title = pygame.font.Font(None, 35)
vie_title = pygame.font.Font(None, 35)
game_over_points_title = pygame.font.Font(None, 40)
record_title = pygame.font.Font(None, 36)
game_over_record = pygame.font.Font(None, 40)
level_title = pygame.font.Font(None, 72)
text_title_object = text_title.render("Pac Man", True, (255, 255, 255))

"""main loop"""

loop_level = 0
loop_menu = 1
loop_game = 1
loop_option = 0
loop_gameover = 0
while loop_game:
    count_animation = 0
    while loop_menu:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                loop_menu = 0
                loop_game = 0
            if event.type == MOUSEBUTTONUP and event.button == 1:

                if 550 < event.pos[0] < 680 and 20 < event.pos[1] < 80:
                    loop_option = 1
                    loop_menu = 0

                if 190 < event.pos[0] < 390 and 415 < event.pos[1] < 510:
                    """Launch of the gamex and initialization of all the variables"""
                    loop_level = 1
                    level_list = init_level()
                    vie_p = 3
                    x_pac_man_i = 6
                    y_pac_man_i = 21
                    x_pac_man = x_pac_man_i
                    y_pac_man = y_pac_man_i
                    x_pac_man_coordinate = x_pac_man * 30
                    y_pac_man_coordinate = y_pac_man * 30
                    direction = ""
                    modif = ""
                    restart = 0
                    coordinate_fan_bleu = [[16, 12], [
                        14 * 30 + 60, 7 * 30 + 150], "high"]
                    coordinate_fan_jaune = [
                        [6, 13], [4 * 30 + 60, 8 * 30 + 150], "high"]
                    coordinate_fan_rose = [[10, 20], [
                        8 * 30 + 60, 15 * 30 + 150], "high"]
                    coordinate_fan_rouge = [
                        [11, 9], [9 * 30 + 60, 4 * 30 + 150], "high"]
                    modif_rouge = ""
                    modif_bleu = ""
                    modif_jaune = ""
                    modif_rose = ""
                    points = 0
                    logic = 1
                    loop_menu = 0

        window.blit(image_menu, (0, 0))
        file = open("record", "r")
        record = file.read()
        file.close()
        record_title_obj = record_title.render(record, True, (255, 255, 255))
        window.blit(record_title_obj, (254, 160))
        pygame.display.flip()

    while loop_option:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == QUIT:
                loop_option = 0
                loop_game = 0
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop_menu = 1
                    loop_option = 0

            if event.type == MOUSEBUTTONUP and event.button == 1:
                if 100 < event.pos[0] < 165 and 275 < event.pos[1] < 325:
                    speed = 2.5
                if 435 < event.pos[0] < 500 and 275 < event.pos[1] < 325:
                    speed = 5
                if 100 < event.pos[0] < 165 and 640 < event.pos[1] < 700:
                    fps = 30
                if 435 < event.pos[0] < 500 and 640 < event.pos[1] < 700:
                    fps = 60

        window.blit(option_image, (0, 0))
        if speed == 2.5:
            window.blit(valide_option_image, (109, 284))
        else:
            window.blit(valide_option_image, (444, 284))
        if fps == 30:
            window.blit(valide_option_image, (109, 649))
        else:
            window.blit(valide_option_image, (444, 649))

        pygame.display.flip()

    while loop_level:
        pygame.time.Clock().tick(fps)
        level_display()

        """key management"""
        for event in pygame.event.get():
            if event.type == QUIT:
                loop_game = 0
                loop_level = 0
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    direction = "left"
                if event.key == K_RIGHT:
                    direction = "right"
                if event.key == K_UP:
                    direction = "high"
                if event.key == K_DOWN:
                    direction = "down"
                if event.key == K_a:
                    direction = "left"
                if event.key == K_d:
                    direction = "right"
                if event.key == K_w:
                    direction = "high"
                if event.key == K_s:
                    direction = "down"

        """character movement"""
        if y_pac_man * 30 == y_pac_man_coordinate and x_pac_man * 30 == x_pac_man_coordinate:
            if direction == "high":
                if condition_advance_high(level_list, x_pac_man, y_pac_man):
                    y_pac_man_coordinate -= speed
                    y_pac_man -= 1
                    modif = "high"
            elif direction == "left":
                if forward_left_condition(level_list, x_pac_man, y_pac_man):
                    x_pac_man -= 1
                    if level_list[y_pac_man][x_pac_man] == 3:
                        x_pac_man = 19
                        y_pac_man = 15
                        x_pac_man_coordinate = x_pac_man * 30
                        y_pac_man_coordinate = y_pac_man * 30
                    else:
                        x_pac_man_coordinate -= speed
                        modif = "left"
            elif direction == "right":
                if condition_forward_right(level_list, x_pac_man, y_pac_man):
                    x_pac_man += 1
                    if level_list[y_pac_man][x_pac_man] == 4:
                        x_pac_man = 4
                        y_pac_man = 15
                        x_pac_man_coordinate = x_pac_man * 30
                        y_pac_man_coordinate = y_pac_man * 30
                    else:
                        x_pac_man_coordinate += speed
                        modif = "right"
            elif direction == "down":
                if condition_advance_low(level_list, x_pac_man, y_pac_man):
                    y_pac_man_coordinate += speed
                    y_pac_man += 1
                    modif = "down"
        else:
            if modif == "high":
                y_pac_man_coordinate -= speed
            elif modif == "left":
                x_pac_man_coordinate -= speed
            elif modif == "right":
                x_pac_man_coordinate += speed
            elif modif == "down":
                y_pac_man_coordinate += speed
        window.blit(pac_man, (x_pac_man_coordinate, y_pac_man_coordinate))

        """gamex points management"""
        if level_list[y_pac_man][x_pac_man] == 2:
            level_list[y_pac_man][x_pac_man] = 0
            points += earnings

        points_var_title = str(points)
        points_title_objet = points_title.render(
            "Puntos :" + points_var_title + " puntos", True, (255, 255, 255))
        window.blit(points_title_objet, (420, 90))

        """management of ghost directions"""
        if direction_time == (30 / speed) * 4:
            direction_time = 0
            coordinate_fan_rouge[2] = direction_choice(
                level_list, coordinate_fan_rouge[0][0], coordinate_fan_rouge[0][1])
            coordinate_fan_rose[2] = direction_choice(
                level_list, coordinate_fan_rose[0][0], coordinate_fan_rose[0][1])
            coordinate_fan_jaune[2] = direction_choice(
                level_list, coordinate_fan_jaune[0][0], coordinate_fan_jaune[0][1])
            coordinate_fan_bleu[2] = direction_choice(
                level_list, coordinate_fan_bleu[0][0], coordinate_fan_bleu[0][1])
        direction_time += 1

        """ghost and display movement management"""
        modif_rouge, coordinate_fan_rouge = phantom_displacement(
            coordinate_fan_rouge, modif_rouge, speed, level_list)
        window.blit(
            fan_rouge, (coordinate_fan_rouge[1][0], coordinate_fan_rouge[1][1]))

        modif_bleu, coordinate_fan_bleu = phantom_displacement(
            coordinate_fan_bleu, modif_bleu, speed, level_list)
        window.blit(
            fan_bleu, (coordinate_fan_bleu[1][0], coordinate_fan_bleu[1][1]))

        modif_jaune, coordinate_fan_jaune = phantom_displacement(
            coordinate_fan_jaune, modif_jaune, speed, level_list)
        window.blit(
            fan_jaune, (coordinate_fan_jaune[1][0], coordinate_fan_jaune[1][1]))

        modif_rose, coordinate_fan_rose = phantom_displacement(
            coordinate_fan_rose, modif_rose, speed, level_list)
        window.blit(
            fan_rose, (coordinate_fan_rose[1][0], coordinate_fan_rose[1][1]))

        """contact with ghost"""
        restart, vie_p = ghost_touch(coordinate_fan_rouge[0][0], coordinate_fan_rouge[0][1], x_pac_man,
                                     y_pac_man, vie_p)
        if restart == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordinate = x_pac_man * 30
            y_pac_man_coordinate = y_pac_man * 30
            coordinate_fan_bleu_i = coordinate_fan_bleu
            coordinate_fan_jaune_i = coordinate_fan_jaune
            coordinate_fan_rose_i = coordinate_fan_rose
            coordinate_fan_rouge_i = coordinate_fan_rouge
        else:
            restart, vie_p = ghost_touch(coordinate_fan_bleu[0][0], coordinate_fan_bleu[0][1], x_pac_man,
                                         y_pac_man, vie_p)
        if restart == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordinate = x_pac_man * 30
            y_pac_man_coordinate = y_pac_man * 30
            coordinate_fan_bleu_i = coordinate_fan_bleu
            coordinate_fan_jaune_i = coordinate_fan_jaune
            coordinate_fan_rose_i = coordinate_fan_rose
            coordinate_fan_rouge_i = coordinate_fan_rouge
        else:
            restart, vie_p = ghost_touch(
                coordinate_fan_jaune[0][0], coordinate_fan_jaune[0][1], x_pac_man, y_pac_man, vie_p)
        if restart == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordinate = x_pac_man * 30
            y_pac_man_coordinate = y_pac_man * 30
            coordinate_fan_bleu_i = coordinate_fan_bleu
            coordinate_fan_jaune_i = coordinate_fan_jaune
            coordinate_fan_rose_i = coordinate_fan_rose
            coordinate_fan_rouge_i = coordinate_fan_rouge
        else:
            restart, vie_p = ghost_touch(
                coordinate_fan_rose[0][0], coordinate_fan_rose[0][1], x_pac_man, y_pac_man, vie_p)
        if restart == 1:
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordinate = x_pac_man * 30
            y_pac_man_coordinate = y_pac_man * 30
            coordinate_fan_bleu_i = coordinate_fan_bleu
            coordinate_fan_jaune_i = coordinate_fan_jaune
            coordinate_fan_rose_i = coordinate_fan_rose
            coordinate_fan_rouge_i = coordinate_fan_rouge

        vie_title_var = str(vie_p)
        vie_title_obj = vie_title.render(
            "Vidas restantes : " + vie_title_var + " vidas", True, (255, 255, 255))
        window.blit(vie_title_obj, (60, 840))

        if vie_p == 0:
            record_int = int(record)
            if points > record_int:
                record_int = points
            loop_gameover = 1
            loop_level = 0

        if points == (logic * 1890) and vie_p != 0:
            """Pause screen display"""
            window.blit(level_suivant_image, (0, 0))
            vie_title_var = str(vie_p)
            points_var_title = str(points)
            level_var_title = str(logic)
            vie_title_obj = vie_title.render(
                vie_title_var + " vies", True, (255, 255, 255))
            points_title_objet = points_title.render(
                points_var_title + "points", True, (255, 255, 255))
            record_title_obj = record_title.render(
                record + "points", True, (255, 255, 255))
            level_title_obj = level_title.render(
                level_var_title, True, (255, 255, 255))
            window.blit(vie_title_obj, (271, 591))
            window.blit(points_title_objet, (231, 64))
            window.blit(record_title_obj, (273, 210))
            window.blit(level_title_obj, (437, 405))

            pygame.display.flip()
            time.sleep(5)

            """level reset"""

            logic += 1
            level_list = init_level()
            x_pac_man_i = 6
            y_pac_man_i = 21
            x_pac_man = x_pac_man_i
            y_pac_man = y_pac_man_i
            x_pac_man_coordinate = x_pac_man * 30
            y_pac_man_coordinate = y_pac_man * 30
            direction = ""
            modif = ""
            restart = 0
            coordinate_fan_bleu = [[16, 12], [
                14 * 30 + 60, 7 * 30 + 150], "high"]
            coordinate_fan_jaune = [
                [6, 13], [4 * 30 + 60, 8 * 30 + 150], "high"]
            coordinate_fan_rose = [[10, 20], [
                8 * 30 + 60, 15 * 30 + 150], "high"]
            coordinate_fan_rouge = [
                [11, 9], [9 * 30 + 60, 4 * 30 + 150], "high"]
            modif_rouge = ""
            modif_bleu = ""
            modif_jaune = ""
            modif_rose = ""

        pygame.display.flip()

    while loop_gameover:
        pygame.time.Clock().tick(fps)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    loop_gameover = 0
                    loop_menu = 1
                if event.key == K_ESCAPE:
                    loop_gameover = 0
                    loop_game = 0
            if event.type == QUIT:
                loop_gameover = 0
                loop_game = 0

        window.blit(game_over_image, (0, 0))
        points_var_title_gameover = str(points)
        points_var_title_gameover_obj = game_over_points_title.render(points_var_title_gameover, True,
                                                                      (255, 255, 255))
        window.blit(points_var_title_gameover_obj, (290, 710))

        record = str(record_int)
        file = open("record", "w")
        file.write(record)
        file.close()
        game_over_record_obj = game_over_record.render(
            record, True, (255, 255, 255))
        window.blit(game_over_record_obj, (257, 753))
        pygame.display.flip()
