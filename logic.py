import random


def init_level():
    level_list = []
    with open("level_1", "r") as file:
        for line in file:
            level_line = []
            for detail in line:
                if detail == "0":
                    level_line.append(0)
                if detail == "1":
                    level_line.append(1)
                if detail == "2":
                    level_line.append(2)
                if detail == "3":
                    level_line.append(3)
                if detail == "4":
                    level_line.append(4)
                if detail == "v":
                    level_line.append("v")
            level_list.append(level_line)
    return level_list


def condition_advance_high(liste, x, y):
    if liste[y - 1][x] == 0 or liste[y - 1][x] == 2:
        return True
    else:
        return False


def condition_advance_low(liste, x, y):
    if liste[y + 1][x] == 0 or liste[y + 1][x] == 2:
        return True
    else:
        return False


def forward_left_condition(liste, x, y):
    if liste[y][x - 1] == 0 or liste[y][x - 1] == 2 or liste[y][x - 1] == 3 or liste[y][x - 1] == 4:
        return True
    else:
        return False


def condition_forward_right(liste, x, y):
    if liste[y][x + 1] == 0 or liste[y][x + 1] == 2 or liste[y][x + 1] == 3 or liste[y][x + 1] == 4:
        return True
    else:
        return False


def direction_choice(liste, x, y):
    proceed = 1
    choix = random.choice(["high", "down", "left", "right"])
    while proceed:
        choix = random.choice(["high", "down", "left", "right"])
        if choix == "high":
            if condition_advance_high(liste, x, y):
                proceed = 0
        elif choix == "down":
            if condition_advance_low(liste, x, y):
                proceed = 0
        elif choix == "left":
            if forward_left_condition(liste, x, y):
                proceed = 0
        elif choix == "right":
            if condition_forward_right(liste, x, y):
                proceed = 0
    return choix


def phantom_displacement(coordinate_fan, modif_f, v, liste):
    if coordinate_fan[0][0] * 30 == coordinate_fan[1][0] and coordinate_fan[0][1] * 30 == \
            coordinate_fan[1][1]:
        if coordinate_fan[2] == "high":
            if condition_advance_high(liste, coordinate_fan[0][0], coordinate_fan[0][1]):
                coordinate_fan[0][1] -= 1
                coordinate_fan[1][1] -= v
                modif_f = "high"
            else:
                coordinate_fan[2] = direction_choice(
                    liste, coordinate_fan[0][0], coordinate_fan[0][1])
        elif coordinate_fan[2] == "down":
            if condition_advance_low(liste, coordinate_fan[0][0], coordinate_fan[0][1]):
                coordinate_fan[0][1] += 1
                coordinate_fan[1][1] += v
                modif_f = "down"
            else:
                coordinate_fan[2] = direction_choice(
                    liste, coordinate_fan[0][0], coordinate_fan[0][1])
        elif coordinate_fan[2] == "left":
            if forward_left_condition(liste, coordinate_fan[0][0], coordinate_fan[0][1]):
                coordinate_fan[0][0] -= 1
                coordinate_fan[1][0] -= v
                modif_f = "left"
            else:
                coordinate_fan[2] = direction_choice(
                    liste, coordinate_fan[0][0], coordinate_fan[0][1])
        elif coordinate_fan[2] == "right":
            if condition_forward_right(liste, coordinate_fan[0][0], coordinate_fan[0][1]):
                coordinate_fan[0][0] += 1
                coordinate_fan[1][0] += v
                modif_f = "right"
            else:
                coordinate_fan[2] = direction_choice(
                    liste, coordinate_fan[0][0], coordinate_fan[0][1])
    else:
        if modif_f == "high":
            coordinate_fan[1][1] -= v
        elif modif_f == "down":
            coordinate_fan[1][1] += v
        elif modif_f == "left":
            coordinate_fan[1][0] -= v
        elif modif_f == "right":
            coordinate_fan[1][0] += v
    return modif_f, coordinate_fan


def ghost_touch(x_f, y_f, x_p, y_p, life):
    if x_f == x_p and y_f == y_p:
        life -= 1
        return 1, life
    else:
        return 0, life
