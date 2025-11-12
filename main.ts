namespace SpriteKind {
    export const player2 = SpriteKind.create()
    export const enemy2 = SpriteKind.create()
}
namespace StatusBarKind {
    export const health2 = StatusBarKind.create()
    export const enemyhealth2 = StatusBarKind.create()
}
/**
 * Define game stages using simple numbers for Python
 */
/**
 * 0: Level 1, 1: Level 2, 2: Game Over
 */
/**
 * Global variable initialization (must be done outside functions if used globally)
 */
// New move for Level 2
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    let damageTaken2: number;
if (currentStage == 1) {
        statusbar2.value += -20
        game.splash("Strong attack! -20 HP to strong dragon!")
        // Enemy retaliates less harshly after strong attack
        damageTaken2 = randint(0, 5)
        game.splash("you took -" + ("" + damageTaken2) + " HP")
        statusbar.value += 0 - damageTaken2
    } else if (currentStage == 0) {
        game.splash("Strong attack not unlocked yet!")
    } else if (currentStage == 3) {
        statusbar2.value += -20
        game.splash("Strong attack! -20 HP to strong dragon!")
        // Enemy retaliates less harshly after strong attack
        damageTaken2 = randint(0, 5)
        game.splash("you took -" + ("" + damageTaken2) + " HP")
        statusbar.value += 0 - damageTaken2
    }
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    let damageBlocked: number;
if (currentStage == 0 || currentStage == 1) {
        damageBlocked = randint(0, 5)
        if (damageBlocked == 0) {
            game.splash("You blocked all damage!")
        } else {
            game.splash("You blocked some damage, took -" + ("" + damageBlocked) + " HP")
            statusbar.value += 0 - damageBlocked
        }
    } else if (currentStage == 0 || currentStage == 3) {
        damageBlocked = randint(0, 5)
        if (damageBlocked == 0) {
            game.splash("You blocked all damage!")
        } else {
            game.splash("You blocked some damage, took -" + ("" + damageBlocked) + " HP")
            statusbar.value += 0 - damageBlocked
        }
    }
})
function setuplevel3 () {
    // Clear previous elements
    sprites.destroyAllSpritesOfKind(SpriteKind.Text)
    // Destroy only the old enemy sprite to keep the player sprite
    if (mySprite2) {
        mySprite2.destroy()
    }
    if (statusbar2) {
        statusbar2.destroy()
    }
    scene.setBackgroundColor(1)
    // Change background color for new level
    textSprite4 = textsprite.create("level #2 select an action", 1, 15)
    textSprite5 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite6 = textsprite.create("<B> = shield", 1, 15)
    textSprite7 = textsprite.create("<UP> = strong attack", 1, 15)
    textSprite8 = textsprite.create("<down> = heal", 1, 15)
    textSprite4.setPosition(80, 10)
    textSprite5.setPosition(60, 30)
    textSprite6.setPosition(42, 40)
    textSprite7.setPosition(66, 50)
    textSprite8.setPosition(45, 60)
    // Setup new enemy for level 2
    mySprite2 = sprites.create(img`
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        `, SpriteKind.Enemy)
    // Create new status bar for level 2 enemy (Goblin King)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
    statusbar2.attachToSprite(mySprite2)
    statusbar2.max = 80
    // Harder boss
    statusbar2.value = 80
    statusbar2.setLabel("king dragon HP", 15)
    mySprite2.setPosition(105, 80)
    currentStage = 3
}
// --- Input Handlers (Modified to check current stage) ---
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    let damageTaken: number;
if (currentStage == 0 || currentStage == 1) {
        statusbar2.value += -10
        game.splash("you did -10 HP to enemy")
        // Simplified enemy retaliation logic
        damageTaken = randint(0, 10)
        game.splash("you took -" + ("" + damageTaken) + " HP")
        statusbar.value += 0 - damageTaken
    }
    if (currentStage == 0 || currentStage == 3) {
        statusbar2.value += -10
        game.splash("you did -10 HP to enemy")
        // Simplified enemy retaliation logic
        damageTaken = randint(0, 10)
        game.splash("you took -" + ("" + damageTaken) + " HP")
        statusbar.value += 0 - damageTaken
    }
})
statusbars.onZero(StatusBarKind.Health, function (status) {
    game.gameOver(false)
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (currentStage == 3) {
        statusbar.value += 20
        game.splash("heal! +20 HP to you!")
    } else if (currentStage == 2) {
        game.splash("heal not unlocked yet!")
    } else if (currentStage == 0) {
        game.splash("heal not unlocked yet!")
    }
})
// Set stage to Level 1
// --- Level 2 Functions (NEW) ---
function setupLevel2 () {
    // Clear previous elements
    sprites.destroyAllSpritesOfKind(SpriteKind.Text)
    // Destroy only the old enemy sprite to keep the player sprite
    if (mySprite2) {
        mySprite2.destroy()
    }
    if (statusbar2) {
        statusbar2.destroy()
    }
    scene.setBackgroundColor(1)
    // Change background color for new level
    textSprite4 = textsprite.create("level #2 select an action", 1, 15)
    textSprite5 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite6 = textsprite.create("<B> = shield", 1, 15)
    textSprite7 = textsprite.create("<UP> = strong attack", 1, 15)
    textSprite4.setPosition(80, 10)
    textSprite5.setPosition(60, 30)
    textSprite6.setPosition(42, 40)
    textSprite7.setPosition(66, 50)
    // Setup new enemy for level 2
    mySprite2 = sprites.create(img`
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        `, SpriteKind.Enemy)
    // Create new status bar for level 2 enemy (Goblin King)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
    statusbar2.attachToSprite(mySprite2)
    statusbar2.max = 80
    // Harder boss
    statusbar2.value = 80
    statusbar2.setLabel("strong dragon HP", 15)
    mySprite2.setPosition(100, 80)
    currentStage = 1
}
function setupLevel1 () {
    // Clear previous elements if any
    sprites.destroyAllSpritesOfKind(SpriteKind.Text)
    sprites.destroyAllSpritesOfKind(SpriteKind.Enemy)
    if (statusbar) {
        statusbar.destroy()
    }
    if (statusbar2) {
        statusbar2.destroy()
    }
    scene.setBackgroundColor(1)
    textSprite = textsprite.create("select a action", 1, 15)
    textSprite2 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite3 = textsprite.create("<B> = shield", 1, 15)
    textSprite.setPosition(80, 10)
    textSprite2.setPosition(60, 30)
    textSprite3.setPosition(42, 40)
    mySprite = sprites.create(img`
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        `, SpriteKind.Player)
    mySprite2 = sprites.create(img`
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 
        `, SpriteKind.Enemy)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.EnemyHealth)
    statusbar2.attachToSprite(mySprite2)
    statusbar2.max = 100
    statusbar2.value = 100
    statusbar2.setLabel("dragon HP", 15)
    mySprite2.setPosition(115, 80)
    statusbar = statusbars.create(20, 4, StatusBarKind.Health)
    statusbar.attachToSprite(mySprite)
    statusbar.setLabel("your HP", 15)
    statusbar.max = 110
    statusbar.value = 110
    mySprite.setPosition(115, 90)
    currentStage = 0
}
let mySprite: Sprite = null
let textSprite3: TextSprite = null
let textSprite2: TextSprite = null
let textSprite: TextSprite = null
let textSprite8: TextSprite = null
let textSprite7: TextSprite = null
let textSprite6: TextSprite = null
let textSprite5: TextSprite = null
let textSprite4: TextSprite = null
let mySprite2: Sprite = null
let statusbar: StatusBarSprite = null
let statusbar2: StatusBarSprite = null
let currentStage = 0
// Start the game at Level 1
setupLevel1()
// Set stage to Level 2
// Handler to check for level changes every 100ms
game.onUpdateInterval(100, function () {
    if (currentStage == 0 && statusbar2.value <= 0) {
        game.splash("Dragon Defeated!", "Proceed to Level 2!")
        setupLevel2()
    } else if (currentStage == 1 && statusbar2.value <= 0) {
        game.splash("strong Dragon Defeated!", "Proceed to Level 3!")
        setuplevel3()
    } else if (currentStage == 3 && statusbar2.value <= 0) {
        game.splash("king Dragon Defeated!")
        game.gameOver(true)
    }
})
