
import simplegui
import random

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH/2
HALF_PAD_HEIGHT = PAD_HEIGHT/2

score1=0
score2=0
score1_pos=[WIDTH/2-60,50]
score2_pos=[WIDTH/2+50,50]


paddle1_pos=[PAD_WIDTH/2,HEIGHT/2]
paddle2_pos=[WIDTH-PAD_WIDTH/2,HEIGHT/2]

paddle1_vel=0
paddle2_vel=0

ball_pos=[0,0]
ball_vel=[0,0]


def ball_init(is_right):
    global ball_pos, ball_vel,WIDTH,HEIGHT
    ball_pos[0]=WIDTH/2
    ball_pos[1]=HEIGHT/2
    ball_vel[1]=1
    if is_right==1:
        ball_vel[0]=1
    else:
        ball_vel[0]=-1

def init():
    global paddle1_pos, paddle2_pos, paddle1_vel,paddle2_vel
    global score1, score2
    is_right=random.randint(0,1)
    ball_init(is_right)

def collision():
    global ball_pos,ball_vel,paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel,score1,score2
    # if ball hit up and down side
    if ball_pos[1]==BALL_RADIUS or ball_pos[1]+BALL_RADIUS==HEIGHT:
        ball_vel[1]=-ball_vel[1]

    if ball_pos[0]==BALL_RADIUS+PAD_WIDTH:
        if ball_pos[1]<paddle1_pos[1]+HALF_PAD_HEIGHT and ball_pos[1]>paddle1_pos[1]-HALF_PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0]
        else:
            score2+=1

    if ball_pos[0]+BALL_RADIUS+PAD_WIDTH==WIDTH:
        if ball_pos[1]<paddle2_pos[1]+HALF_PAD_HEIGHT and ball_pos[1]>paddle2_pos[1]-HALF_PAD_HEIGHT:
            ball_vel[0]=-ball_vel[0]
        else:
            score1+=1

    if ball_pos[0]==BALL_RADIUS or ball_pos[0]+BALL_RADIUS==WIDTH:
        is_right=random.randint(0,1)
        ball_init(is_right)





def draw(canvas):
    global ball_pos,ball_vel,paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel
    # draw the frame
    canvas.draw_line([WIDTH/2,0],[WIDTH/2,HEIGHT],1,"White")
    canvas.draw_line([PAD_WIDTH/2,0],[PAD_WIDTH,HEIGHT],1,"White")
    canvas.draw_line([WIDTH-PAD_WIDTH,0],[WIDTH-PAD_WIDTH,HEIGHT],1,"White")


    # update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    canvas.draw_circle(ball_pos,BALL_RADIUS,10,"Red","Red")

    # update paddle position
    paddle1_pos[1] += paddle1_vel
    paddle2_pos[1] += paddle2_vel
    p1=[0,0]
    p2=[0,0]
    p1=[HALF_PAD_WIDTH,paddle1_pos[1]-HALF_PAD_HEIGHT]
    p2=[HALF_PAD_WIDTH,paddle1_pos[1]+HALF_PAD_HEIGHT]
    canvas.draw_line(p1,p2,PAD_WIDTH,"White")
    p1=[WIDTH-HALF_PAD_WIDTH,paddle2_pos[1]-HALF_PAD_HEIGHT]
    p2=[WIDTH-HALF_PAD_WIDTH,paddle2_pos[1]+HALF_PAD_HEIGHT]
    canvas.draw_line(p1,p2,PAD_WIDTH,"White")

    # handle collision
    collision()

    # draw score
    canvas.draw_text(str(score1),score1_pos,20,"White")
    canvas.draw_text(str(score2),score2_pos,20,"White")


def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel -= 1
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel += 1
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel-=1
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel+=1

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["up"]:
        paddle2_vel =0
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    elif key==simplegui.KEY_MAP["w"]:
        paddle1_vel = 0
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel =0


frame = simplegui.create_frame("Pong",WIDTH,HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart",init,100)
frame.add_label("How to play:")
frame.add_label("Press w and s to control the left side")
frame.add_label("Press Arrow Up and Down to control the right side")


init()
frame.start()
