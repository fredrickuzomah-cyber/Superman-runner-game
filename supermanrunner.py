import pyautogui,random,pgzrun


WIDTH,HEIGHT=pyautogui.size()

obstacles=["explosion","alien_ship","meteor"]
enemies=[]

def create_obstacles():
    obstacle=Actor(random.choice(obstacles))
    obstacle.pos=WIDTH,random.randint(0,HEIGHT)
    enemies.append(obstacle)

superman=Actor("superman.png")
superman.pos=90,HEIGHT/2
superman.angle=90

def draw():
    screen.clear()
    superman.draw()
    for e in enemies:
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


clock.schedule_interval(create_obstacles,1)

pgzrun.go()