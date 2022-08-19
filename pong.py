from cs1lib import *

# defines variables for game window
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

# defines variables for paddles
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
LX = 0
INITIAL_LY = 0
ly = 0
RX = WINDOW_WIDTH - PADDLE_WIDTH
INITIAL_RY = WINDOW_HEIGHT - PADDLE_HEIGHT
ry = WINDOW_HEIGHT - PADDLE_HEIGHT
PADDLE_SPEED = 5
FIX_SLITHER = 1

# defines variables for ball
INITIAL_BALL_X = 200
INITIAL_BALL_Y = 200
ball_x = 200
ball_y = 200
BALL_RADIUS = 10
INITIAL_BALL_X_SPEED = 4
INITIAL_BALL_Y_SPEED = 4
ball_x_speed = 4
ball_y_speed = 4

# defines variables for button presses
a_press = False
z_press = False
k_press = False
m_press = False
space_count = 0
q_press = False

# defines variables for running and restarting the game
run = False
restart = False


# function to check if a key is pressed
def key_down(key):
    global a_press, z_press, k_press, m_press, space_count, q_press
    if key == 'a':
        a_press = True
    if key == 'z':
        z_press = True
    if key == 'k':
        k_press = True
    if key == 'm':
        m_press = True
    # if the space bar is pressed space_count increases which changes if the game restarts
    if key == ' ':
        space_count = space_count + 1
    if key == 'q':
        q_press = True


# checks if a key is released
def key_up(key):
    global a_press, z_press, k_press, m_press
    if key == 'a':
        a_press = False
    if key == 'z':
        z_press = False
    if key == 'k':
        k_press = False
    if key == 'm':
        m_press = False


# draws the background, the paddles, and the ball
def draw_game():
    # set background
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_stroke_width(1)
    draw_line(WINDOW_WIDTH / 2, 0, WINDOW_WIDTH / 2, WINDOW_HEIGHT)

    # draw left paddle
    set_fill_color(1, 0, 0)
    draw_rectangle(LX, ly, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw right paddle
    set_fill_color(0, 0, 1)
    draw_rectangle(RX, ry, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw ball
    set_fill_color(1, 1, 1)
    draw_circle(ball_x, ball_y, BALL_RADIUS)


# moves the paddles up and down when respective keys are pressed
def move_paddles():
    global ly, ry
    if a_press and ly > 0:
        ly = ly - PADDLE_SPEED
    if z_press and ly < WINDOW_HEIGHT - PADDLE_HEIGHT:
        ly = ly + PADDLE_SPEED
    if k_press and ry > 0:
        ry = ry - PADDLE_SPEED
    if m_press and ry < WINDOW_HEIGHT - PADDLE_HEIGHT:
        ry = ry + PADDLE_SPEED


# moves the ball when the game starts running
def move_ball():
    global ball_x, ball_y
    if run:
        ball_x = ball_x + ball_x_speed
        ball_y = ball_y + ball_y_speed


# makes a game over screen whenever the game ends
def stop_game():
    global ball_x_speed, ball_y_speed
    clear()
    ball_x_speed = 0
    ball_y_speed = 0
    set_font_size(50)
    draw_text("Game Over", WINDOW_WIDTH / 6, WINDOW_HEIGHT / 2)


# checks if the ball hits a horizontal wall and makes it bounce off the wall
def hit_horizontal_wall():
    global ball_y_speed
    if ball_y - BALL_RADIUS < 0:
        ball_y_speed = - ball_y_speed
    if ball_y + BALL_RADIUS > WINDOW_HEIGHT:
        ball_y_speed = - ball_y_speed


# checks if the ball hits a horizontal wall and stops the game
def hit_vertical_wall():
    global ball_x_speed
    if ball_x + BALL_RADIUS < 0:
        stop_game()
    if ball_x + BALL_RADIUS > WINDOW_WIDTH:
        stop_game()


# checks if the ball hits a paddle and makes it bounce of the paddle
def hit_paddle():
    global ball_x_speed, ball_x
    if (ball_x - BALL_RADIUS < 0 + PADDLE_WIDTH) and (ball_y > ly) and (ball_y < ly + PADDLE_HEIGHT):
        ball_x = PADDLE_WIDTH + BALL_RADIUS + FIX_SLITHER  # makes ball leave inside of paddle to fix slither
        ball_x_speed = -ball_x_speed
    if (ball_x + BALL_RADIUS >= WINDOW_WIDTH - PADDLE_WIDTH) and (ball_y > ry) and (ball_y < ry + PADDLE_HEIGHT):
        ball_x = WINDOW_WIDTH - PADDLE_WIDTH - BALL_RADIUS - FIX_SLITHER
        ball_x_speed = -ball_x_speed


# resets position of game objects to their initial values and makes a start game screen
def restart_game():
    global ball_x, ball_y, ly, ry, ball_x_speed, ball_y_speed
    ball_x = INITIAL_BALL_X
    ball_y = INITIAL_BALL_Y
    ly = INITIAL_LY
    ry = INITIAL_RY
    ball_x_speed = INITIAL_BALL_X_SPEED
    ball_y_speed = INITIAL_BALL_Y_SPEED
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_font_size(29)
    draw_text("Press space bar to start game", 10, WINDOW_HEIGHT / 2)


# quits the game whenever the space bar is pressed
def quit_game():
    if q_press:
        cs1_quit()


# calls all helper functions when game is running
def start_game():
    global run
    run = True
    draw_game()
    move_paddles()
    move_ball()
    hit_horizontal_wall()
    hit_vertical_wall()
    hit_paddle()


# checks if game is running and restarts/starts game whenever space bar is pressed
def run_game():
    if space_count == 0 or space_count % 2 == 0:
        restart_game()
    elif space_count % 2 != 0:
        start_game()
    quit_game()


start_graphics(run_game, key_press=key_down, key_release=key_up, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
