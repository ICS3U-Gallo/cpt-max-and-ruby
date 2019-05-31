# cpt-max-and-ruby
cpt-max-and-ruby created by GitHub Classroom
import arcade


WIDTH = 640
HEIGHT = 480
player_x = 100
player_y = 400
x = 100
y = 100
button1 = [200, 260, 240, 80]
button2 = [200, 140, 240, 80]
button3 = [200, 20, 240, 80]
back = [0, 440, 60, 40]

move_speed = [0, 0]

UP = False
DOWN = False
LEFT = False
RIGHT = False

text = [430, 550, 40, 60]

current_screen = "menu"

def update(delta_time):
    global player_y, UP, DOWN, player_x, LEFT, RIGHT
    if current_screen == "game":
        if UP:
            player_y += 5
        if DOWN:
            player_y -= 0
        if LEFT:
            player_x += -2
        if RIGHT:
            player_x += 2
        # grav
        move_speed[1] -= 0.3

        #interactionn with floor
        if player_y - 5 <=  45 and player_x > 0 and player_x < 440 or player_y - 5 <= 45 and player_x > 540 and player_x < 640:
            move_speed[1] = 0
        elif player_y - 5 <= 270 and player_y - 5 >= 250 and player_x > 0 and player_x < 280 or player_y - 5 <= 270 and player_x > 540 and player_x < 640:
            move_speed[1] = 0


        player_x += move_speed[0]
        player_y += move_speed[1]



        # check ladder collision
        if player_y - 5 <= y  and player_y -5 >= 55 and player_x > 280 and player_x < 320:
            move_speed[1] = 0

        if player_y - 5 == 45 and player_x > 400 and player_x < 440:
            arcade.draw_text("wanna go for a swim?", 420, 60, arcade.color.BLACK, 12)

def on_draw():
    global WIDTH, HEIGHT

    arcade.start_render()

    if current_screen == "menu":
        arcade.draw_text("2D Maze Escape", 200, 380, arcade.color.BLACK, 22)
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

        arcade.draw_xywh_rectangle_filled(280, 45, 5, 225, arcade.color.LIGHT_BROWN)
        arcade.draw_xywh_rectangle_filled(320, 45, 5, 225, arcade.color.LIGHT_BROWN)
        for y in range(50, 275, 15):
            arcade.draw_xywh_rectangle_filled(280, y, 40, 5, arcade.color.LIGHT_BROWN)

        #tree with key
        arcade.draw_xywh_rectangle_filled(400, 130, 10, 3, arcade.color.YELLOW)
        arcade.draw_xywh_rectangle_filled(380, 45, 20, 50, arcade.color.BROWN_NOSE)
        arcade.draw_triangle_filled(360, 95, 390, 155, 420, 95, arcade.color.APPLE_GREEN)

        arcade.draw_xywh_rectangle_filled(player_x, player_y, 5, 10, arcade.color.BLACK)  # body
        arcade.draw_xywh_rectangle_filled(player_x - 2, player_y + 10, 9, 9, arcade.color.BLACK)  # head
        arcade.draw_xywh_rectangle_filled(player_x - 5, player_y + 4, 15, 2, arcade.color.BLACK)  # arms
        arcade.draw_xywh_rectangle_filled(player_x - 5, player_y - 5, 5, 5, arcade.color.BLACK)  # left leg
        arcade.draw_xywh_rectangle_filled(player_x + 5, player_y - 5, 5, 5, arcade.color.BLACK)  # right leg

    elif current_screen == "how to play":
        arcade.draw_text("INSTRUCTIONS", 150, 400, arcade.color.BLACK, 35)
        arcade.draw_xywh_rectangle_filled(0, 440, 60, 40, arcade.color.BLACK)
        arcade.draw_text("back", 10, 455, arcade.color.WHITE, 12)

def draw_ladder():
    arcade.draw_xywh_rectangle_filled(280, 45, 5, 225, arcade.color.LIGHT_BROWN)
    arcade.draw_xywh_rectangle_filled(320, 45, 5, 225, arcade.color.LIGHT_BROWN)
    for y in range(50, 275, 15):
        arcade.draw_xywh_rectangle_filled(280, y, 40, 5, arcade.color.LIGHT_BROWN)



def on_key_press(key, modifiers):
    global LEFT, RIGHT, UP, DOWN, player_x, player_y, current_screen

    if key == arcade.key.LEFT:
        LEFT = True

    if key == arcade.key.RIGHT:
        RIGHT = True

    if key == arcade.key.UP:
        UP = True

    if key == arcade.key.DOWN:
        DOWN = True



def on_key_release(key, modifiers):
    global LEFT, RIGHT, DOWN, UP

    if key == arcade.key.LEFT:
        LEFT = False

    elif key == arcade.key.RIGHT:
        RIGHT = False

    elif key == arcade.key.UP:
        UP = False

    elif key == arcade.key.DOWN:
        DOWN = False



def on_mouse_press(x, y, button, modifiers):
    global current_screen
    if x > button1[0] and x < button1[0] + button1[2] and y > button1[1] and y < button1[1] + button1[3]:
        current_screen = "game"
    elif x > button2[0] and x < button2[0] + button2[2] and y > button2[1] and y < button2[1] + button2[3]:
        current_screen = "how to play"
    elif x > button3[0] and x < button3[0] + button3[2] and y > button3[1] and y < button3[1] + button3[3]:
        arcade.close_window()
    elif x > back[0] and x < back[0] + back[2] and y > back[1] and y < back[1] + back[3]:
        current_screen = "menu"


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

