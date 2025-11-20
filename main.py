@namespace
class SpriteKind:
    player2 = SpriteKind.create()
    enemy2 = SpriteKind.create()
    tree = SpriteKind.create()
@namespace
class StatusBarKind:
    health2 = StatusBarKind.create()
    enemyhealth2 = StatusBarKind.create()
"""

Define game stages using simple numbers for Python

"""
"""

0: Level 1, 1: Level 2, 2: Game Over

"""
"""

Global variable initialization (must be done outside functions if used globally)

"""
# New move for Level 2

def on_up_pressed():
    if currentStage == 1:
        statusbar2.value += -20
        game.splash("Strong attack! -20 HP to strong dragon!")
        # Enemy retaliates less harshly after strong attack
        damageTaken2 = randint(0, 5)
        game.splash("you took -" + ("" + str(damageTaken2)) + " HP")
        statusbar.value += 0 - damageTaken2
    elif currentStage == 0:
        game.splash("Strong attack not unlocked yet!")
    elif currentStage == 3:
        statusbar2.value += -20
        game.splash("Strong attack! -20 HP to strong dragon!")
        # Enemy retaliates less harshly after strong attack
        damageTaken2 = randint(0, 5)
        game.splash("you took -" + ("" + str(damageTaken2)) + " HP")
        statusbar.value += 0 - damageTaken2
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_b_pressed():
    if currentStage == 0 or currentStage == 1:
        damageBlocked = randint(0, 5)
        if damageBlocked == 0:
            game.splash("You blocked all damage!")
        else:
            game.splash("You blocked some damage, took -" + ("" + str(damageBlocked)) + " HP")
            statusbar.value += 0 - damageBlocked
    elif currentStage == 0 or currentStage == 3:
        damageBlocked = randint(0, 5)
        if damageBlocked == 0:
            game.splash("You blocked all damage!")
        else:
            game.splash("You blocked some damage, took -" + ("" + str(damageBlocked)) + " HP")
            statusbar.value += 0 - damageBlocked
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def setuplevel3():
    global textSprite4, textSprite5, textSprite6, textSprite7, textSprite8, mySprite2, statusbar2, currentStage
    # Clear previous elements
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    # Destroy only the old enemy sprite to keep the player sprite
    if mySprite2:
        mySprite2.destroy()
    if statusbar2:
        statusbar2.destroy()
    scene.set_background_color(1)
    # Change background color for new level
    textSprite4 = textsprite.create("level #3 select an action", 1, 15)
    textSprite5 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite6 = textsprite.create("<B> = shield", 1, 15)
    textSprite7 = textsprite.create("<UP> = strong attack", 1, 15)
    textSprite8 = textsprite.create("<down> = heal", 1, 15)
    textSprite4.set_position(80, 10)
    textSprite5.set_position(60, 30)
    textSprite6.set_position(42, 40)
    textSprite7.set_position(66, 50)
    textSprite8.set_position(45, 60)
    # Setup new enemy for level 2
    mySprite2 = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    # Create new status bar for level 2 enemy (Goblin King)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.max = 80
    # Harder boss
    statusbar2.value = 80
    statusbar2.set_label("king dragon HP", 15)
    mySprite2.set_position(105, 80)
    currentStage = 3
# --- Input Handlers (Modified to check current stage) ---

def on_a_pressed():
    if currentStage == 0 or currentStage == 1:
        statusbar2.value += -10
        game.splash("you did -10 HP to enemy")
        # Simplified enemy retaliation logic
        damageTaken = randint(0, 10)
        game.splash("you took -" + ("" + str(damageTaken)) + " HP")
        statusbar.value += 0 - damageTaken
    if currentStage == 0 or currentStage == 3:
        statusbar2.value += -10
        game.splash("you did -10 HP to enemy")
        # Simplified enemy retaliation logic
        damageTaken = randint(0, 10)
        game.splash("you took -" + ("" + str(damageTaken)) + " HP")
        statusbar.value += 0 - damageTaken
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_button_released():
    controller.move_sprite(mySprite)
controller.any_button.on_event(ControllerButtonEvent.RELEASED, on_button_released)

def on_on_zero(status):
    game.game_over(False)
statusbars.on_zero(StatusBarKind.health, on_on_zero)

def on_down_pressed():
    if currentStage == 3:
        statusbar.value += 20
        game.splash("heal! +20 HP to you!")
    elif currentStage == 2:
        game.splash("heal not unlocked yet!")
    elif currentStage == 0:
        game.splash("heal not unlocked yet!")
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

# Set stage to Level 1
# --- Level 2 Functions (NEW) ---
def setupLevel2():
    global textSprite4, textSprite5, textSprite6, textSprite7, mySprite2, statusbar2, currentStage
    # Clear previous elements
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    # Destroy only the old enemy sprite to keep the player sprite
    if mySprite2:
        mySprite2.destroy()
    if statusbar2:
        statusbar2.destroy()
    scene.set_background_color(1)
    # Change background color for new level
    textSprite4 = textsprite.create("level #2 select an action", 1, 15)
    textSprite5 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite6 = textsprite.create("<B> = shield", 1, 15)
    textSprite7 = textsprite.create("<UP> = strong attack", 1, 15)
    textSprite4.set_position(80, 10)
    textSprite5.set_position(60, 30)
    textSprite6.set_position(42, 40)
    textSprite7.set_position(66, 50)
    # Setup new enemy for level 2
    mySprite2 = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    # Create new status bar for level 2 enemy (Goblin King)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.max = 80
    # Harder boss
    statusbar2.value = 80
    statusbar2.set_label("strong dragon HP", 15)
    mySprite2.set_position(89, 80)
    currentStage = 1
def setupLevel1():
    global mySprite2, textSprite, textSprite2, textSprite3, statusbar2, statusbar, currentStage
    # Clear previous elements if any
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    if statusbar:
        statusbar.destroy()
    if statusbar2:
        statusbar2.destroy()
    mySprite2 = sprites.create(img("""
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
            """),
        SpriteKind.enemy)
    scene.set_background_color(1)
    textSprite = textsprite.create("select a action", 1, 15)
    textSprite2 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite3 = textsprite.create("<B> = shield", 1, 15)
    textSprite.set_position(80, 10)
    textSprite2.set_position(60, 30)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.max = 100
    statusbar2.value = 100
    statusbar2.set_label("dragon HP", 15)
    mySprite2.set_position(110, 80)
    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.attach_to_sprite(mySprite)
    statusbar.set_label("your HP", 15)
    statusbar.max = 110
    statusbar.value = 110
    mySprite.set_position(116, 90)
    currentStage = 0
    textSprite3.set_position(42, 40)
textSprite3: TextSprite = None
textSprite2: TextSprite = None
textSprite: TextSprite = None
textSprite8: TextSprite = None
textSprite7: TextSprite = None
textSprite6: TextSprite = None
textSprite5: TextSprite = None
textSprite4: TextSprite = None
mySprite2: Sprite = None
statusbar: StatusBarSprite = None
statusbar2: StatusBarSprite = None
currentStage = 0
mySprite: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
    """))
mySprite = sprites.create(img("""
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
        """),
    SpriteKind.player)
scene.camera_follow_sprite(mySprite)
# Set stage to Level 2
# Handler to check for level changes every 100ms

def on_update_interval():
    if currentStage == 0 and statusbar2.value <= 0:
        game.splash("Dragon Defeated!", "Proceed to Level 2!")
        setupLevel2()
    elif currentStage == 1 and statusbar2.value <= 0:
        game.splash("strong Dragon Defeated!", "Proceed to Level 3!")
        setuplevel3()
    elif currentStage == 3 and statusbar2.value <= 0:
        game.splash("king Dragon Defeated!")
        game.game_over(True)
game.on_update_interval(100, on_update_interval)
