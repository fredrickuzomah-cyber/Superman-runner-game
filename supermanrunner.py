import pyautogui,random,pgzrun
WIDTH,HEIGHT=pyautogui.size()

superman=Actor("superman.png")
superman.pos=90,HEIGHT/2
superman.angle=90
def draw():
    superman.draw()

def update():
    if keyboard.up:
        superman.y-=10
    if keyboard.down:
        superman.y+=10
    if superman.y<0:
        superman.y=HEIGHT
    if superman.y>HEIGHT:
        superman.y=0


pgzrun.go()