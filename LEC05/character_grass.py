from pico2d import *

open_canvas()
grass = load_image('grass.png')
character = load_image('character.png')

while True:
    
    x= 400
    while x< 600:
        clear_canvas()
        character.draw(x, 300)
        update_canvas()
        x+=2
        delay(0.01)

    y= 300
    while y< 500:
        clear_canvas()
        character.draw(600, y)
        update_canvas()
        y+=2
        delay(0.01)

    x= 600
    while x>200:
        clear_canvas()
        character.draw(x, 500)
        update_canvas()
        x-=2
        delay(0.01)

    y= 500
    while y> 100:
        clear_canvas()
        character.draw(200, y)
        update_canvas()
        y-=2
        delay(0.01)



close_canvas()
