# template for "Stopwatch: The Game"

import simplegui

# define global variables
t = 0  #tenth of second
x = 0  #number of times the watch is stopped on a whole second
y = 0  #number of times the watch is stopped in total
ctr = False
color = 'White'

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    "Converting inc to A:BC.D format"
    D = t % 10
    C = (t // 10) % 10
    B = (t // 100) % 6
    A = (t // 600) % 10
    return str(A)+':'+str(B)+str(C)+'.'+str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    if not timer.is_running():
        timer.start()
        global ctr, color
        ctr = True
        color = 'White'

def stop_handler():
    timer.stop()
    global y, x, ctr, color
    if ctr:
        ctr = False
        y += 1
        if (t % 10) == 0:
            x += 1
            color = 'Green'
        else:
            color = 'Red'
    
def restart_handler():
    timer.stop()
    global t, x, y, color
    t = 0
    x = 0
    y = 0
    color = 'White'

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global t
    t += 1
    

# define draw handler
def draw_handler(canvas):
    timeStr = format(t)
    canvas.draw_text(timeStr, (25, 120), 60, color, 'serif')
    xyStr = str(x)+'/'+str(y)
    canvas.draw_text(xyStr, (160, 30), 20, 'Green', 'serif')
    
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200,150)


# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
button1 = frame.add_button('Start', start_handler,150)
button2 = frame.add_button('Stop', stop_handler,150)
button3 = frame.add_button('Restart', restart_handler,150)

# start frame
frame.start()

# Please remember to review the grading rubric
