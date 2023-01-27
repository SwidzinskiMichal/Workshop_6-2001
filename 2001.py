import random

def dice_roller():
    dice = list(range(1, 7))
    rolls = random.choices(dice, k = 2)
    return sum(rolls)


def dice_game():
    player1_points = dice_roller()
    player2_points = dice_roller()
    print(f"PLY: {player1_points}")
    print(f"CPU: {player2_points}")
    temp_res = 0
    while not player1_points >= 2001 and not player2_points >= 2001:
        input("Press enter to roll!")
        temp_res = dice_roller()
        if temp_res == 7:
            player1_points = int(player1_points/7)
        elif temp_res == 11:
            player1_points = player1_points * 11
        else:
            player1_points = player1_points + temp_res
        print(f"PLY: {player1_points}")

        print("CPU is rolling!")
        temp_res = dice_roller()
        if temp_res == 7:
            player2_points = int(player2_points/7)
        elif temp_res == 11:
            player2_points = player2_points * 11
        else:
            player2_points = player2_points + temp_res
        print(f"CPU: {player2_points}")
    print(f"PLY: {player1_points}")
    print(f"CPU: {player2_points}")
    return None


dice_game()