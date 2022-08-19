from cs1lib import *
from random import *

# Extra credit: added ball acceleration, ball changing colors, random initial movement, score board, win condition,
# ball starting at color of last score, and reflection and default modes

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
PADDLE_SPEED = 10
FIX_SLITHER = 1  # variable to fix the slither error
# variables to change color of paddles
LR = 1
LB = 0
RR = 0
RB = 1
PG = 0

# defines variables for ball
INITIAL_BALL_X = 200
INITIAL_BALL_Y = 200
ball_x = 200
ball_y = 200
BALL_RADIUS = 10
INITIAL_SPEED_X = 5
speed_x = 5
INITIAL_SPEED_Y = 5
speed_y = 5
# variables to make the ball start in a random spot each time and increase speed when a paddle is hit
ball_acceleration = 1
INITIAL_BALL_ACCELERATION = 1
ACCELERATION = .5
ball_x_speed = 4
ball_y_speed = 4
# variables to change color of ball
RESET_COLOR = 6  # variable for max color
WHITE = 0
RED = 1
ORANGE = 2
YELLOW = 3
GREEN = 4
BLUE = 5
VIOLET = 6
color = WHITE
R = 1
G = 1
B = 1


# defines variables for button presses
a_press = False
z_press = False
k_press = False
m_press = False
# if the space bar is pressed space_count increases which changes if the game restarts
space_count = 0
q_press = False
r_press = False
u_press = True

# variables to run game and restart game
run = False
restart = False

# variables to keep track of player score and game winner
p1_score = 0
p2_score = 0
WIN_CONDITION = 7


# checks if a key is pressed
def key_down(key):
    global a_press, z_press, k_press, m_press, space_count, q_press, r_press, u_press
    if key == 'a':
        a_press = True
    if key == 'z':
        z_press = True
    if key == 'k':
        k_press = True
    if key == 'm':
        m_press = True
    if key == ' ':
        space_count = space_count + 1
    if key == 'q':
        q_press = True
    # determines is game is reversed or not
    if key == 'r':
        r_press = True
        u_press = False
    if key == 'u':
        u_press = True
        r_press = False


# check if a key is released
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


# draws all game objects
def draw_game():
    # set background
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_stroke_width(1)
    draw_line(WINDOW_WIDTH / 2, 0, WINDOW_WIDTH / 2, WINDOW_HEIGHT)

    # draw scoreboard
    set_font_size(40)
    draw_text(str(p1_score), (WINDOW_WIDTH / 2) - 50, 40)
    draw_text(str(p2_score), (WINDOW_WIDTH / 2) + 50, 40)

    # draw left paddle
    set_fill_color(LR, PG, LB)
    draw_rectangle(LX, ly, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw right paddle
    set_fill_color(RR, PG, RB)
    draw_rectangle(RX, ry, PADDLE_WIDTH, PADDLE_HEIGHT)

    # draw ball
    set_fill_color(R, G, B)
    draw_circle(ball_x, ball_y, BALL_RADIUS)


# function that changes the ball color whenever ball hits paddle
def change_ball_color():
    global R, G, B, color
    if color == WHITE:
        R = 1
        G = 1
        B = 1
    if color == RED:
        R = 1
        G = 0
        B = 0
    if color == ORANGE:
        R = 1
        G = .647
        B = 0
    if color == YELLOW:
        R = 1
        G = 1
        B = 0
    if color == GREEN:
        R = 0
        G = 1
        B = 0
    if color == BLUE:
        R = 0
        G = 0
        B = 1
    if color == VIOLET:
        R = .933
        G = .51
        B = .933
    if color > RESET_COLOR:
        color = WHITE


# moves paddle whenever the movement keys are pressed
def move_paddles():
    global ly, ry
    if u_press:  # default setting a and z move left paddle and k and m move right paddle
        if a_press and ly > 0:
            ly = ly - PADDLE_SPEED
        if z_press and ly < WINDOW_HEIGHT - PADDLE_HEIGHT:
            ly = ly + PADDLE_SPEED
        if k_press and ry > 0:
            ry = ry - PADDLE_SPEED
        if m_press and ry < WINDOW_HEIGHT - PADDLE_HEIGHT:
            ry = ry + PADDLE_SPEED
    elif r_press:  # reversed setting a and z move right paddle and k and m move left paddle
        if a_press and ry > 0:
            ry = ry - PADDLE_SPEED
        if z_press and ry < WINDOW_HEIGHT - PADDLE_HEIGHT:
            ry = ry + PADDLE_SPEED
        if k_press and ly > 0:
            ly = ly - PADDLE_SPEED
        if m_press and ly < WINDOW_HEIGHT - PADDLE_HEIGHT:
            ly = ly + PADDLE_SPEED


# changes the color of the paddles to match P1(Red) and p2(Blue) when game is reflected
def reflect_game():
    global LR, LB, RR, RB
    if r_press:
        LR = 0
        LB = 1
        RR = 1
        RB = 0
    if u_press:
        LR = 1
        LB = 0
        RR = 0
        RB = 1


# function to move ball when game is running and to increase speed of ball when paddle is hit
def move_ball():
    global ball_x, ball_y
    if run:
        ball_x = ball_x + (ball_x_speed * ball_acceleration)
        ball_y = ball_y + ball_y_speed


# increases player 1 score when ball hits blue(p2) wall
def player1_score():
    global p1_score, space_count, ball_x, ball_y, ly, ry, ball_x_speed, ball_y_speed, color, ball_acceleration
    ball_x = INITIAL_BALL_X
    ball_y = INITIAL_BALL_Y
    ly = INITIAL_LY
    ry = INITIAL_RY
    ball_acceleration = INITIAL_BALL_ACCELERATION
    ball_x_speed = INITIAL_SPEED_X
    ball_y_speed = randint(-INITIAL_SPEED_X, INITIAL_SPEED_X)
    color = 5
    set_clear_color(0, 0, 0)
    clear()
    p1_score = p1_score + 1


# increases player 2 score when ball hits red(p1) wall
def player2_score():
    global p2_score, space_count, ball_x, ball_y, ly, ry, ball_x_speed, ball_y_speed, color, ball_acceleration
    ball_x = INITIAL_BALL_X
    ball_y = INITIAL_BALL_Y
    ly = INITIAL_LY
    ry = INITIAL_RY
    ball_acceleration = INITIAL_BALL_ACCELERATION
    ball_x_speed = -INITIAL_SPEED_X
    ball_y_speed = randint(-INITIAL_SPEED_X, INITIAL_SPEED_X)
    color = 5
    set_clear_color(0, 0, 0)
    clear()
    p2_score = p2_score + 1


# determines the winner of the game when a player reaches the WIN CONDITION(score of 7)
def win_game():
    global ball_x_speed, ball_y_speed
    if p1_score >= WIN_CONDITION:
        clear()
        ball_x_speed = 0
        ball_y_speed = 0
        set_font_size(50)
        draw_text("Player 1 Wins", WINDOW_WIDTH / 6, WINDOW_HEIGHT / 2)
    if p2_score >= WIN_CONDITION:
        clear()
        ball_x_speed = 0
        ball_y_speed = 0
        set_font_size(50)
        draw_text("Player 2 Wins", WINDOW_WIDTH / 6, WINDOW_HEIGHT / 2)


# makes the ball bounce when the ball hits a horizontal wall
def hit_horizontal_wall():
    global ball_y_speed
    if ball_y - BALL_RADIUS < 0:
        ball_y_speed = - ball_y_speed
    if ball_y + BALL_RADIUS > WINDOW_HEIGHT:
        ball_y_speed = - ball_y_speed


# gives a player a point when the ball hits a vertical wall
def hit_vertical_wall():
    global p2_score, p1_score
    global ball_x_speed
    if ball_x + BALL_RADIUS < 0:
        if u_press:  # default if ball hits left side p2 scores(blue)
            player2_score()
        elif r_press:
            player1_score()  # reflection if ball hits left side p1 scores(red)
    if ball_x + BALL_RADIUS > WINDOW_WIDTH:
        if u_press:
            player1_score()  # default if ball hits right side p1(red) scores
        elif r_press:
            player2_score() # reflection is ball hits right side p2(blue) scores


# makes the ball bounce, change color, and increase speed when paddle is hit
def hit_paddle():
    global ball_x_speed, color, p1_score, p2_score, ball_acceleration, ball_x
    if (ball_x - BALL_RADIUS < 0 + PADDLE_WIDTH) and (ball_y > ly) and (ball_y < ly + PADDLE_HEIGHT):
        ball_x_speed = -ball_x_speed  # bounces ball
        ball_x = PADDLE_WIDTH + BALL_RADIUS + FIX_SLITHER  # makes ball move outside of paddle to fix slither error
        color = color + 1  # changes color
        ball_acceleration = ball_acceleration + ACCELERATION  # makes ball speed up
    if (ball_x + BALL_RADIUS >= WINDOW_WIDTH - PADDLE_WIDTH) and (ball_y > ry) and (ball_y < ry + PADDLE_HEIGHT):
        ball_x = WINDOW_WIDTH - PADDLE_WIDTH - BALL_RADIUS - FIX_SLITHER  # fixes slither error
        ball_x_speed = -ball_x_speed  # bounces ball
        color = color + 1  # changes color
        ball_acceleration = ball_acceleration + ACCELERATION  # makes ball speed up


# objects reset to their initial value and displays start game screen
def restart_game():
    global ball_x, ball_y, ly, ry, ball_x_speed, ball_y_speed, color, p1_score, p2_score, ball_acceleration, r_press,\
        u_press, speed_x, speed_y
    r_press = False
    u_press = True
    ball_x = INITIAL_BALL_X
    ball_y = INITIAL_BALL_Y
    ly = INITIAL_LY
    ry = INITIAL_RY
    speed_x = randint(-INITIAL_SPEED_X, INITIAL_SPEED_X)
    speed_y = randint(-INITIAL_SPEED_Y, INITIAL_SPEED_Y)
    if speed_x != 0:
        ball_x_speed = speed_x
    else:
        ball_x_speed = INITIAL_SPEED_X
    if speed_y != 0:
        ball_y_speed = speed_y
    else:
        ball_y_speed = INITIAL_SPEED_Y
    ball_acceleration = INITIAL_BALL_ACCELERATION
    p1_score = 0
    p2_score = 0
    color = 0
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    set_font_size(29)
    draw_text("Press space bar to start game", 10, WINDOW_HEIGHT / 2)


# makes the game quit when q is pressed
def quit_game():
    if q_press:
        cs1_quit()


# calls all functions that make game run
def start_game():
    global run
    run = True
    change_ball_color()
    draw_game()
    move_paddles()
    move_ball()
    hit_horizontal_wall()
    hit_vertical_wall()
    hit_paddle()
    reflect_game()


# displays start screen when space count is 0 or even and makes game run when space count is odd
def run_game():
    if space_count == 0 or space_count % 2 == 0:
        restart_game()
    elif space_count % 2 != 0:
        start_game()
    quit_game()
    win_game()


start_graphics(run_game, key_press=key_down, key_release=key_up)
