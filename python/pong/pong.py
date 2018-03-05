# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PADDLE_VEL = 4

ball_pos = [0,0]
ball_vel = [0,0]
paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT

paddle1_vel = 0
paddle2_vel = 0

score1 = 0
score2 = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel[0] = random.randrange(120, 240) / 60
    ball_vel[1] = -random.randrange(60, 180) / 60
    if not direction:
        ball_vel[0] = -ball_vel[0]
        
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    leftright = [LEFT,RIGHT]
    random.shuffle(leftright)
    spawn_ball(leftright[0])
    
def collision(direction):
    if direction:
        #ball has collided with left gutter
        if (ball_pos[1] + BALL_RADIUS >= paddle1_pos) and (ball_pos[1] - BALL_RADIUS <= paddle1_pos + PAD_HEIGHT):
            ball_vel[0] = - 1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
            return 0;
        else:
            spawn_ball(direction)
            return 1
    else:
        if (ball_pos[1] + BALL_RADIUS >= paddle2_pos) and (ball_pos[1] - BALL_RADIUS <= paddle2_pos + PAD_HEIGHT):
            ball_vel[0] = -1.1 * ball_vel[0]
            ball_vel[1] = 1.1 * ball_vel[1]
            return 0;
        else:
            spawn_ball(direction)
            return 1

def button_handler():
    new_game()
    

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
       
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    #Collision detection in vertical direction
    if ball_pos[1] <= BALL_RADIUS - 1:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] = BALL_RADIUS -1
    if ball_pos[1] >= HEIGHT - BALL_RADIUS  + 1:
        ball_vel[1] = - ball_vel[1]
        ball_pos[1] = HEIGHT - BALL_RADIUS  + 1
    #Collision detection with gutters in horizental direction
    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH +1:
        tmp = collision(RIGHT)
        score2 += tmp
    if ball_pos[0] >= WIDTH - PAD_WIDTH - BALL_RADIUS  + 1:
        tmp = collision(LEFT)
        score1 += tmp
        
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS-1, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    
    if paddle1_pos <= 1:   # 1 (not 0) to account fot line
        paddle1_pos = 1
    elif paddle1_pos >= HEIGHT - (PAD_HEIGHT+1):
        paddle1_pos = HEIGHT - (PAD_HEIGHT+1)
    
    if paddle2_pos <= 1:   # 1 (not 0) to account fot line
        paddle2_pos = 1
    elif paddle2_pos >= HEIGHT - (PAD_HEIGHT+1):
        paddle2_pos = HEIGHT - (PAD_HEIGHT+1)
        
    # draw paddles
    canvas.draw_polygon([[1, paddle1_pos],[PAD_WIDTH-1, paddle1_pos], [PAD_WIDTH-1, paddle1_pos+PAD_HEIGHT], [1, paddle1_pos+PAD_HEIGHT]], 1, 'White', 'White')
    canvas.draw_polygon([[WIDTH-1, paddle2_pos],[WIDTH-PAD_WIDTH+1, paddle2_pos], [WIDTH-PAD_WIDTH+1, paddle2_pos+PAD_HEIGHT], [WIDTH-1, paddle2_pos+PAD_HEIGHT]], 1, 'White', 'White')
    # draw scores
    scoredraw = str(score1)+'      '+str(score2)
    canvas.draw_text(scoredraw, (WIDTH/2-10*len(scoredraw), 120), 60, 'Green')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP['s']):
        paddle1_vel = PADDLE_VEL
    elif (key == simplegui.KEY_MAP['w']):
        paddle1_vel = -PADDLE_VEL
        
    if (key == simplegui.KEY_MAP['down']):
        paddle2_vel = PADDLE_VEL
    elif (key == simplegui.KEY_MAP['up']):
        paddle2_vel = -PADDLE_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if (key == simplegui.KEY_MAP['s']) or (key == simplegui.KEY_MAP['w']):
        paddle1_vel = 0
    if (key == simplegui.KEY_MAP['up']) or (key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0
    


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
button2 = frame.add_button('Reset', button_handler, 150)


# start frame
new_game()
frame.start()
