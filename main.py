@namespace
class StatusBarKind:
    distance = StatusBarKind.create()

def on_b_pressed():
    global playa, hidden, distancebar, posrandmulti
    tiles.set_current_tilemap(tilemap("""
        level2
    """))
    playa = sprites.create(img("""
            . . . . c c c b b b b b . . . . 
                    . . c c b 4 4 4 4 4 4 b b b . . 
                    . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                    . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                    e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                    . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                    8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                    8 7 2 e e e e e e e e e e 2 7 8 
                    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                    e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                    e b e 8 8 c c 8 8 c c c 8 e b e 
                    e e b e c c e e e e e c e b e e 
                    . e e b b 4 4 4 4 4 4 4 4 e e . 
                    . . . c c c c c e e e e e . . .
        """),
        SpriteKind.player)
    hidden = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        SpriteKind.enemy)
    distancebar = statusbars.create(80, 4, StatusBarKind.health)
    distancebar.set_color(2, 7, 3)
    distancebar.set_position(80, 105)
    playa.set_position(75, 55)
    posrandmulti = 11
    hidden.set_position(randint(30, 220), randint(30, 220))
    controller.move_sprite(playa, 100, 100)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_a_released():
    hidden.set_image(img("""
        . . 2 2 b b b b b . . . . . . . 
                . 2 b 4 4 4 4 4 4 b . . . . . . 
                2 2 4 4 4 4 d d 4 4 b . . . . . 
                2 b 4 4 4 4 4 4 d 4 b . . . . . 
                2 b 4 4 4 4 4 4 4 d 4 b . . . . 
                2 b 4 4 4 4 4 4 4 4 4 b . . . . 
                2 b 4 4 4 4 4 4 4 4 4 e . . . . 
                2 2 b 4 4 4 4 4 4 4 b e . . . . 
                . 2 b b b 4 4 4 b b b e . . . . 
                . . e b b b b b b b e e . . . . 
                . . . e e b 4 4 b e e e b . . . 
                . . . . . e e e e e e b d b b . 
                . . . . . . . . . . . b 1 1 1 b 
                . . . . . . . . . . . c 1 d d b 
                . . . . . . . . . . . c 1 b c . 
                . . . . . . . . . . . . c c . .
    """))
controller.A.on_event(ControllerButtonEvent.RELEASED, on_a_released)

distf = 0
diste = 0
distd = 0
distc = 0
distb = 0
dista = 0
y2 = 0
x2 = 0
y1 = 0
x1 = 0
posrandmulti = 0
distancebar: StatusBarSprite = None
hidden: Sprite = None
playa: Sprite = None
c = "G"
r = "L"
e = "X"
a = "Z"
t = "Y"
o = "@wood52995 on twitter"
r = "https://github.com/woodj3wh8r"

def on_forever():
    playa.say_text("" + str(hidden.x) + "," + ("" + str(hidden.y)))

forever(on_forever)

def on_forever2():
    global x1, x2, y1, y2, dista, distb, distc, distd, diste, distf
    final = 0
    scene.center_camera_at(x1, y1)
    x1 = playa.x
    x2 = hidden.x
    y1 = playa.y
    y2 = hidden.y
    distancebar.value = final / 1
    dista = x2 - x1
    distb = y2 - y1
    distc = Math.imul(dista, 2)
    distd = distb * distb
    diste = distc + distd
    distf = Math.sqrt(diste)
    distancebar.value = distf
forever(on_forever2)
