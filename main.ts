namespace StatusBarKind {
    export const distance = StatusBarKind.create()
}

let distf = 0
let diste = 0
let distd = 0
let distc = 0
let distb = 0
let dista = 0
let y2 = 0
let x2 = 0
let y1 = 0
let x1 = 0
let text_sprite = null
tiles.setCurrentTilemap(tilemap`
    level2
`)
let c = "G"
let r = "L"
let e = "X"
let a = "Z"
let t = "Y"
let o = "@wood52995 on twitter"
r = "https://github.com/woodj3wh8r"
let playa = sprites.create(img`
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
    `, SpriteKind.Player)
let hidden = sprites.create(img`
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
    `, SpriteKind.Enemy)
let distancebar = statusbars.create(80, 4, StatusBarKind.Health)
distancebar.setColor(2, 7, 3)
distancebar.setPosition(80, 105)
playa.setPosition(0, 0)
let posrandmulti = 12
hidden.setPosition(randint(-10, 10) * posrandmulti, randint(-10, 10) * posrandmulti)
controller.moveSprite(playa, 100, 100)
forever(function on_forever() {
    
    let final = 0
    scene.centerCameraAt(x1, y1)
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
})
