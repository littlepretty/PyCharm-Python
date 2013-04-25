__author__ = 'yan'

import simplegui

# global variables
time = 0
time_str = ""
success = 0
tempt = 0
game_str = ""

interval = 100
height = 400
width = 400

# helper function
def convert():
    global time_str, game_str
    if time>10*60:
        min = time//10//60
    else:
        min = 0
    sec = (time-min*600)//10
    tenthSec = time%10
    if sec<10:
        time_str = str(min)+":0"+str(sec)+"."+str(tenthSec)
    else:
        time_str = str(min)+":"+str(sec)+"."+str(tenthSec)
        # print(time_str)
    game_str=str(success)+"/"+str(tempt)
    # print(game_str)

# draw handler
def draw_watch(canvas):
    convert()
    canvas.draw_text(game_str,[4/5*width, 1/4*height],28,"Green")
    canvas.draw_text(time_str,[2/5*width, 1/2*height],36,"White")

# time handler
def tenth_second():
    global time
    time += 1

# button handlers
def click_start():
    global timer, tempt
    tempt += 1
    timer.start()

def click_stop():
    global success
    if time%10 == 0:
        success += 1
    timer.stop()

def click_reset():
    global time
    time =0

# create frame and timer
frame = simplegui.create_frame("StopWatch",width,height)
timer = simplegui.create_timer(interval,tenth_second)


# register handlers
frame.add_button("Start",click_start,100)
frame.add_button("Stop",click_stop,100)
frame.add_button("Reset",click_reset,100)
frame.set_draw_handler(draw_watch)


frame.start()














