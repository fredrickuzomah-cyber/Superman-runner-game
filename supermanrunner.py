import pyautogui,random,pgzrun



WIDTH,HEIGHT=pyautogui.size()

obstacles=["explosion","alien_ship","meteor"]
enemies=[]
lasers=[]

def create_obstacles():
    obstacle=Actor(random.choice(obstacles))
    if obstacle.image=="meteor":
        obstacle.right=-45
    obstacle.pos=WIDTH,random.randint(0,HEIGHT)
    enemies.append(obstacle)

superman=Actor("superman.png")
superman.pos=90,HEIGHT/2
superman.angle=90

def draw():
    screen.blit("skybackground.jpg",(0,0))
    superman.draw()
    for e in enemies:
        e.draw()
    for e in lasers:
        e.draw()
def update():
    if keyboard.up:
        superman.y-=10
    if keyboard.down:
        superman.y+=10
    if superman.y<0:
        superman.y=HEIGHT
    if superman.y>HEIGHT:
        superman.y=0
    for i in enemies:
        i.x-=10
        if i.x<0:
            enemies.remove(i)
    for i in lasers:
        i.x+=10
        if i.x > WIDTH:
            lasers.remove(i)
        for e in enemies:
            if i.colliderect(e):
                lasers.remove(i)
                enemies.remove(e)
def on_key_down(key):
    if key==keys.SPACE:
        laser=Actor("redbeam.png")
        laser.pos=superman.x-20,superman.y-200
        lasers.append(laser)

clock.schedule_interval(create_obstacles,4)

pgzrun.go()