# implementation of card game - Memory

import simplegui
import random

rng = 8

cardlst = range(rng)+range(rng)

exposed = []
xpos = []
memorylst = []
count = 0
for i in range(16):
       exposed.append(False)
       xpos.append(i*800/16)

# helper function to initialize globals
def new_game():
    global count, memorylst, exposed
    count = 0
    label.set_text('Turns = '+ str(count))
    memorylst = []
   
    for i in range(16):
        exposed[i] = False
    random.shuffle(cardlst)

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global memorylst, count
    
    if not exposed[pos[0] // (800/16)]:
        count += 1
        memorylst.append(pos[0] // (800/16))
        exposed[pos[0] // (800/16)] = True
        if len(memorylst) == 2:
            if cardlst[memorylst[0]] == cardlst[memorylst[1]]:
                memorylst = []
        if len(memorylst) > 2:
            exposed[memorylst[0]] = False
            if cardlst[memorylst[1]] != cardlst[memorylst[2]]:
                memorylst.pop(0)
            else:
                memorylst = []
    label.set_text('Turns = '+ str(count))
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    posnum = 0
    for i in range(16):
        if not exposed[i]:
            canvas.draw_polygon([[xpos[i], 0], [xpos[i]+800/16, 0], [xpos[i]+800/16, 100], [xpos[i], 100]], 1, 'Green','Green')
       
        else:
            canvas.draw_text(str(cardlst[i]), [15+posnum, 70], 40, 'White')
        posnum = posnum +50
    pass


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric