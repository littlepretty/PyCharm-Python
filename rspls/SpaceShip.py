import math
import simplegui

class ImageInfo:
    def __init__(self,center,size,radius=0,lifespan=None,animated=False):
        self.center=center
        self.size=size
        self.radius=radius
        if lifespan:
            self.lifespan=lifespan
        else:
            self.lifespan=float('inf')
        self.animated=animated

    def get_center(self):
        return self.center

    def __getattr__(self, item):
        if item=="center":
            return self.center
        elif item=="size":
            return self.size
        elif item=="radius":
            return self.radius
        elif item=="lifespan":
            return self.lifespan
        elif item=="animated":
            return self.animated

class Ship:
    def __init__(self,pos,vel,angle,image,info):
        self.pos=[pos[0],pos[1]]
        self.vel=[vel[0],vel[1]]
        self.thrust=False
        self.friction_constant=0.05
        self.angle=angle
        self.angle_vel=0
        self.image=image
        self.image_center=info.center
        self.image_size=info.size
        self.radius=info.radius

    def draw(self,canvas):
        canvas.draw_circle(self.pos,self.radius,1,"White","White")

    def update(self):
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]

        self.vel[0]*=(1-self.friction_constant)
        self.vel[1]*=(1-self.friction_constant)

        if self.thrust:
            forward=[math.cos(self.angle),math.sin(self.angle)]
            self.vel[0]+=forward[0]
            self.vel[1]+=forward[1]


class Sprite:
    def __init__(self,pos,vel,angle,angle_vel,image,info,sound=None):
        self.pos=[pos[0],pos[1]]
        self.vel=[vel[0],vel[1]]
        self.angle=angle
        self.angle_vel=angle_vel
        self.image=image
        self.image_center=info.center
        self.image_size=info.size
        self.radius=info.radius
        self.lifespan=info.lifespan
        self.animated=info.animated
        self.age=0
        if sound:
            sound.rewind()
            sound.play()

    def draw(self,canvas):
        canvas.draw_image(self.image,self.image_center,self.image_size,self.pos,self.image_size,self.angle)

    def update(self):
        self.angle+=self.angle_vel
        self.pos[0]+=self.vel[0]
        self.pos[1]+=self.vel[1]

def draw(canvas):
    rock.draw(canvas)
    rock.update()

frame=simplegui.create_frame("Sprite Demo",800,600)

asteroid_info=ImageInfo([45,45],[90,90],40)
asteroid_image=simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")
rock=Sprite([300,400],[0.5,0.5],0,0.1,asteroid_image,asteroid_info)

frame.set_draw_handler(draw)
frame.start()


















