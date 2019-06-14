import arcade


WIDTH = 640
HEIGHT = 480
player_x = 15
player_y = 50
x = 100
y = 100
button1 = [200, 260, 240, 80]
button2 = [200, 140, 240, 80]
button3 = [200, 20, 240, 80]
back = [0, 440, 60, 40]

move_speed = [0, 0]
Emove_speed = 1
enemy = [100, 45]
enemy2 = [125, 270]
chest1 = [5, 270, 30, 25]
chest2 = [600, 45, 30, 25]
door = [600, 270, 30, 40]
plat1 = [75, 300, 30, 5]
plat2 = [75, 330, 30, 5]
plat3 = [75, 360, 30, 5]
plat4 = [75, 390, 30, 5]
plat5 = [75, 420, 30, 5]
plat6 = [75, 450, 30, 5]
plat7 = [75, 470, 30, 5]

items = ["key"]
inventory = []
wood = False
jump_boots = False

UP = False
DOWN = False
LEFT = False
RIGHT = False
E = False
Enemy_left = False
Enemy_right = True

current_screen = "menu"

def update(delta_time):
    global player_y, UP, DOWN, player_x, LEFT, RIGHT, WIDTH, HEIGHT, current_screen, enemy, Emove_speed, jump_boots, door
    if current_screen == "game":
        if UP:
            player_y += 5
        if DOWN:
            player_y -= 0
        if LEFT:
            player_x -= 2
        if RIGHT:
            player_x += 2
        # grav
        move_speed[1] -= 0.3

        #interactionn with floor
        if player_y - 5 <=  45 and player_x > 0 and player_x < 440 or player_y - 5 <= 45 and player_x > 540 and player_x < 640:
            move_speed[1] = 0
        elif player_y - 5 <= 270 and player_y - 5 >= 250 and player_x > 0 and player_x < 280 or player_y - 5 <= 270 and player_y - 5 >= 250 and player_x > 540 and player_x < 640:
            move_speed[1] = 0
        if wood == True and player_x > 435 and player_x < 545 and player_y > 45 and player_y < 55:
            move_speed[1] = 0

        player_x += move_speed[0]
        player_y += move_speed[1]

        # check ladder collision
        if player_y - 5 <= y  and player_y -5 >= 255 and player_x > 280 and player_x < 320:
            move_speed[1] = 0

        #death effect
        if player_y - 5 < 0:
            current_screen = "death"
            print("YOU DIED")
            player_y = 50
            player_x = 25
        if player_y - 5 > 480:
            current_screen = "death"
            player_y = 50
            player_x = 25

        #ladder physics
        if player_x >= 280 and player_x <= 320 and player_y >= 50 and player_y <= 270:
            move_speed[1] = 0.3
            if DOWN:
                player_y -= 2

        #enemy
        if enemy[0] <= 100:
            Emove_speed = 1
        elif enemy[0] >= 150:
            Emove_speed = -1
        enemy[0] += Emove_speed
        if player_x > enemy[0] and player_x < enemy[0] + 15 and player_y > enemy[1] and player_y < enemy[1] + 15:
            current_screen = "death"
            player_x = 15
            player_y = 50

        #enemy2
        if enemy2[0] <= 125:
            Emove_speed = 1
        elif enemy2[0] >= 175:
            Emove_speed = -1
        enemy2[0] += Emove_speed
        if player_x > enemy2[0] and player_x < enemy2[0] + 15 and player_y > enemy2[1] and player_y < enemy2[1] + 15:
            current_screen = "death"
            player_x = 15
            player_y = 50

        #getting wood
        if E and player_x > 380 and player_x < 400 and "axe" in inventory:
            inventory.remove("axe")
            inventory.append("wood")
            print(f"inventory: {inventory}")

        #getting jump boots
        if player_x > chest2[0] and player_x < chest2[0] + chest2[2] and E:
            inventory.append(jump_boots)

        if jump_boots in inventory and UP:
            player_y += 7

        #exit
        if E and player_x > door[0] and player_x < door[0] + door[2] and player_y > door[1] and player_y < door[1] + door[3]:
            current_screen = "win"

        if player_x > plat1[0] and player_x < plat1[0] + plat1[2] and player_y > plat1[1] and player_y < plat1[1] + plat1[3]:
            move_speed[1] = 0.3
        if player_x > plat2[0] and player_x < plat2[0] + plat2[2] and player_y > plat2[1] and player_y < plat2[1] + plat2[3]:
            move_speed[1] = 0.3
        if player_x > plat3[0] and player_x < plat3[0] + plat3[2] and player_y > plat3[1] and player_y < plat3[1] + plat3[3]:
            move_speed[1] = 0.3
        if player_x > plat4[0] and player_x < plat4[0] + plat4[2] and player_y > plat4[1] and player_y < plat4[1] + plat4[3]:
            move_speed[1] = 0.3
        if player_x > plat5[0] and player_x < plat5[0] + plat5[2] and player_y > plat5[1] and player_y < plat5[1] + plat5[3]:
            move_speed[1] = 0.3
        if player_x > plat6[0] and player_x < plat6[0] + plat6[2] and player_y > plat6[1] and player_y < plat6[1] + plat6[3]:
            move_speed[1] = 0.3
        if player_x > plat7[0] and player_x < plat7[0] + plat7[2] and player_y > plat7[1] and player_y < plat7[1] + plat7[3]:
            move_speed[1] = 0.3



def on_draw():
    global WIDTH, HEIGHT, player_x, player_y, wood

    arcade.start_render()

    if current_screen == "menu":
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_text("2D Escape room", 200, 380, arcade.color.BLACK, 22)
        arcade.draw_xywh_rectangle_filled(button1[0], button1[1], button1[2], button1[3], arcade.color.BLACK)
        arcade.draw_text("START", 275, 285, arcade.color.WHITE, 22)
        arcade.draw_xywh_rectangle_filled(button2[0], button2[1], button2[2], button2[3], arcade.color.BLACK)
        arcade.draw_text("How To Play", 230, 165, arcade.color.WHITE, 22)
        arcade.draw_xywh_rectangle_filled(button3[0], button3[1], button3[2], button3[3], arcade.color.BLACK)
        arcade.draw_text("Exit Game", 250, 45, arcade.color.WHITE, 22)
    elif current_screen == "game":

    # Draw in here...
        arcade.set_background_color(arcade.color.SKY_BLUE)
       #ground
        for x in range(0, 440, 20):
            arcade.draw_xywh_rectangle_filled(x, 0, 10, 10, arcade.color.BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 0, 10, 10, arcade.color.COCOA_BROWN)
        for x in range(0, 440, 20):
            arcade.draw_xywh_rectangle_filled(x, 20, 10, 10, arcade.color.BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 20, 10, 10, arcade.color.COCOA_BROWN)
        for x in range(0, 440, 20):
            arcade.draw_xywh_rectangle_filled(x, 10, 10, 10, arcade.color.COCOA_BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 10, 10, 10, arcade.color.BROWN)
        for x in range(540, 640, 20):
            arcade.draw_xywh_rectangle_filled(x, 0, 10, 10, arcade.color.BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 0, 10, 10, arcade.color.COCOA_BROWN)
        for x in range(540, 640, 20):
            arcade.draw_xywh_rectangle_filled(x, 20, 10, 10, arcade.color.BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 20, 10, 10, arcade.color.COCOA_BROWN)
        for x in range(540, 640, 20):
            arcade.draw_xywh_rectangle_filled(x, 10, 10, 10, arcade.color.COCOA_BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 10, 10, 10, arcade.color.BROWN)

        #grass and water
        arcade.draw_xywh_rectangle_filled(0, 30, 440, 15, arcade.color.APPLE_GREEN)
        arcade.draw_xywh_rectangle_filled(440, 0, 100, 40, arcade.color.OCEAN_BOAT_BLUE)
        arcade.draw_xywh_rectangle_filled(540, 30, 100, 15, arcade.color.APPLE_GREEN)

        #back button
        arcade.draw_xywh_rectangle_filled(0, 440, 60, 40, arcade.color.BLACK)
        arcade.draw_text("back", 10, 455, arcade.color.WHITE, 12)

        #upper platform
        for x in range(0, 280, 20):
            arcade.draw_xywh_rectangle_filled(x, 240, 10, 30, arcade.color.LIGHT_BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 240, 10, 30, arcade.color.COCOA_BROWN)
        for x in range(0, 280, 20):
            arcade.draw_xywh_rectangle_filled(x, 240, 10, 30, arcade.color.LIGHT_BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 240, 10, 30, arcade.color.COCOA_BROWN)
        for x in range(540, 640, 20):
            arcade.draw_xywh_rectangle_filled(x, 240, 10, 30, arcade.color.LIGHT_BROWN)
            arcade.draw_xywh_rectangle_filled(x + 10, 240, 10, 30, arcade.color.COCOA_BROWN)

        #ladder
        draw_ladder(280, 45, 50, 225)

        #chests
        chest(chest1[0], chest1[1], chest1[2], chest1[3])
        chest(chest2[0], chest2[1], chest2[2], chest2[3])

        #tree
        arcade.draw_xywh_rectangle_filled(380, 45, 20, 50, arcade.color.BROWN_NOSE)
        arcade.draw_triangle_filled(360, 95, 390, 155, 420, 95, arcade.color.APPLE_GREEN)

        #pop up text
        if player_x > 430 and player_x < 440 and "wood" not in inventory:
            arcade.draw_text("Wanna go for a swim?", 430, 70, arcade.color.BLACK, 7)
        elif player_x > 0 and player_x < 20 and player_y < 100:
            arcade.draw_text("Start", 0, 100, arcade.color.GOLD, 15)
            arcade.draw_xywh_rectangle_filled(0, 95, 55, 2, arcade.color.GOLD)
        elif "axe" in inventory and player_x > 350 and player_y < 380:
            arcade.draw_text("Lumberjack time!", 350 , 70, arcade.color.BLACK, 7)
        elif "wood" in inventory and player_x > 430 and player_x < 440:
            arcade.draw_text("place wood?", 400, 75, arcade.color.BLACK, 7)

        arcade.draw_text("go up for a surprise^^", 25, 400, arcade.color.BLACK, 8)

        #enemy
        draw_enemy(enemy)
        draw_enemy(enemy2)

        #key physics
        if "key" in items:
            arcade.draw_xywh_rectangle_filled(400, 130, 10, 3, arcade.color.YELLOW)
        if player_x > 400 and player_x < 410 and player_y > 130 and player_y < 133:
            items.remove("key")
            inventory.append("key")
        arcade.draw_text(f"inventory: {inventory}", 300, 400, arcade.color.BLACK, 15)
        if "key" in inventory and E and player_x > chest1[0] and player_x < chest1[0] + chest1[2] and player_y > chest1[1] and player_y < chest1[1] + chest1[3]:
            inventory.remove("key")
            inventory.append("axe")
            print(f"inventory: {inventory}")

        if "wood" in inventory and player_x > 430 and player_x < 440 and E:
            wood = True

        if wood == True:
            arcade.draw_xywh_rectangle_filled(435, 45, 110, 5, arcade.color.BROWN)

        #exit door
        arcade.draw_xywh_rectangle_filled(door[0], door[1], door[2], door[3], arcade.color.DARK_BROWN)
        arcade.draw_circle_filled(door[0] + 7, door[1] + 20, 2, arcade.color.GOLD)
        arcade.draw_text("EXIT", door[0], door[1] + 45, arcade.color.RED, 8)

        #platforms
        draw_platform(plat1[0], plat1[1], plat1[2], plat1[3])
        draw_platform(plat2[0], plat2[1], plat2[2], plat2[3])
        draw_platform(plat3[0], plat3[1], plat3[2], plat3[3])
        draw_platform(plat4[0], plat4[1], plat4[2], plat4[3])
        draw_platform(plat5[0], plat5[1], plat5[2], plat5[3])
        draw_platform(plat6[0], plat6[1], plat6[2], plat6[3])
        draw_platform(plat7[0], plat7[1], plat7[2], plat7[3])

        # character
        arcade.draw_xywh_rectangle_filled(player_x, player_y, 5, 10, arcade.color.BLACK)  # body
        arcade.draw_xywh_rectangle_filled(player_x - 2, player_y + 10, 9, 9, arcade.color.BLACK)  # head
        arcade.draw_xywh_rectangle_filled(player_x - 5, player_y + 4, 15, 2, arcade.color.BLACK)  # arms
        arcade.draw_xywh_rectangle_filled(player_x - 5, player_y - 5, 5, 5, arcade.color.BLACK)  # left leg
        arcade.draw_xywh_rectangle_filled(player_x + 5, player_y - 5, 5, 5, arcade.color.BLACK)  # right leg

        if jump_boots in inventory:
            arcade.draw_xywh_rectangle_filled(player_x - 5, player_y - 5, 5, 5, arcade.color.RED)  # left leg
            arcade.draw_xywh_rectangle_filled(player_x + 5, player_y - 5, 5, 5, arcade.color.RED)  # right leg
            arcade.draw_text("jump boots equiped", 530, 75, arcade.color.BLACK, 7)

    elif current_screen == "death":
        arcade.set_background_color(arcade.color.RED_DEVIL)
        arcade.draw_xywh_rectangle_filled(0, 440, 60, 40, arcade.color.BLACK)
        arcade.draw_text("back", 10, 455, arcade.color.WHITE, 12)
        arcade.draw_text("YOU DIED!!!", 200, 240, arcade.color.BLACK, 30)


    elif current_screen == "how to play":
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_text("INSTRUCTIONS", 150, 400, arcade.color.BLACK, 35)
        arcade.draw_xywh_rectangle_filled(0, 440, 60, 40, arcade.color.BLACK)
        arcade.draw_text("back", 10, 455, arcade.color.WHITE, 12)
        arcade.draw_text("Use arrow keys to move", 100, 340, arcade.color.BLACK, 15)
        arcade.draw_text("Press E to interact with objects", 100, 300, arcade.color.BLACK, 15)
        arcade.draw_text("If you leave the screen you die", 100, 260, arcade.color.BLACK, 15)
        arcade.draw_text("If you die your progress will be saved", 100, 220, arcade.color.BLACK, 15)
        arcade.draw_text("Dont touch anything red!", 100, 180, arcade.color.BLACK, 15)
        arcade.draw_text("Your goal- get to the exit door", 100, 140, arcade.color.BLACK, 15)
        arcade.draw_text("GOOD LUCK!", 150, 60, arcade.color.BLACK, 20)


    elif current_screen == "win":
        arcade.draw_xywh_rectangle_filled(0, 440, 60, 40, arcade.color.BLACK)
        arcade.draw_text("back", 10, 455, arcade.color.WHITE, 12)
        arcade.draw_text("CONGRATS!!!", 25, 200, arcade.color.GOLD, 70)
        arcade.set_background_color(arcade.color.SKY_BLUE)
        arcade.draw_text("see that wasn't too hard", 200, 175, arcade.color.BLACK, 15)



def draw_ladder(x, y, w, h):
    arcade.draw_xywh_rectangle_filled(x, y, 5, h, arcade.color.LIGHT_BROWN)
    arcade.draw_xywh_rectangle_filled(x + 40, y, 5, h, arcade.color.LIGHT_BROWN)
    for yl in range(50, 275, 15):
        arcade.draw_xywh_rectangle_filled(x, yl, 40, 5, arcade.color.LIGHT_BROWN)

def draw_enemy(position):
    arcade.draw_xywh_rectangle_filled(position[0],position[1], 15, 15, arcade.color.RED)

def draw_platform(x, y, w, h):
    arcade.draw_xywh_rectangle_filled(x, y, w, h, arcade.color.BROWN)

def chest(x, y, w, h):
    arcade.draw_xywh_rectangle_filled(x, y, w, h, arcade.color.DARK_BROWN)
    arcade.draw_xywh_rectangle_filled(x + 12.5, y + 10, 5, 5, arcade.color.GRAY)
    arcade.draw_xywh_rectangle_filled(x, y, 2.5, h, arcade.color.GOLD)
    arcade.draw_xywh_rectangle_filled(x + 27.5, y, 2.5, h, arcade.color.GOLD)
    arcade.draw_xywh_rectangle_filled(x, y + 10, w, 1, arcade.color.BLACK)



def on_key_press(key, modifiers):
    global LEFT, RIGHT, UP, DOWN, player_x, player_y, current_screen, E

    if key == arcade.key.LEFT:
        LEFT = True

    if key == arcade.key.RIGHT:
        RIGHT = True

    if key == arcade.key.UP:
        UP = True

    if key == arcade.key.DOWN:
        DOWN = True

    if key == arcade.key.E:
        E = True



def on_key_release(key, modifiers):
    global LEFT, RIGHT, DOWN, UP, E

    if key == arcade.key.LEFT:
        LEFT = False

    elif key == arcade.key.RIGHT:
        RIGHT = False

    elif key == arcade.key.UP:
        UP = False

    elif key == arcade.key.DOWN:
        DOWN = False

    elif key == arcade.key.E:
        E = False



def on_mouse_press(x, y, button, modifiers):
    global current_screen, player_x, player_y
    if x > button1[0] and x < button1[0] + button1[2] and y > button1[1] and y < button1[1] + button1[3]:
        current_screen = "game"
    elif x > button2[0] and x < button2[0] + button2[2] and y > button2[1] and y < button2[1] + button2[3]:
        current_screen = "how to play"
    elif x > button3[0] and x < button3[0] + button3[2] and y > button3[1] and y < button3[1] + button3[3]:
        arcade.close_window()
    elif x > back[0] and x < back[0] + back[2] and y > back[1] and y < back[1] + back[3]:
        current_screen = "menu"
        player_x = 15
        player_y = 50

def on_mouse_move(x, y, delta_x, delta_y):
    if current_screen == "menu":
        print(x, y)

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release
    window.on_mouse_press = on_mouse_press

    arcade.run()


if __name__ == '__main__':
    setup()
