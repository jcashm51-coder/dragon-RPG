@namespace
class SpriteKind:
    player2 = SpriteKind.create()
    enemy2 = SpriteKind.create()
@namespace
class StatusBarKind:
    health2 = StatusBarKind.create()
    enemyhealth2 = StatusBarKind.create()

# Define game stages using simple numbers for Python
# 0: Level 1, 1: Level 2, 2: Game Over
currentStage = 0

def setupLevel1():
    global textSprite, textSprite2, textSprite3, mySprite, mySprite2, statusbar, statusbar2, currentStage
    
    # Clear previous elements if any
    sprites.destroy_all_sprites_of_kind(SpriteKind.text)
    sprites.destroy_all_sprites_of_kind(SpriteKind.enemy)
    if statusbar:
        statusbar.destroy()
    if statusbar2:
        statusbar2.destroy()

    scene.set_background_color(1)
    textSprite = textsprite.create("select a action", 1, 15)
    textSprite2 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite3 = textsprite.create("<B> = shield", 1, 15)
    textSprite.set_position(80, 10)
    textSprite2.set_position(60, 30)
    textSprite3.set_position(42, 40)

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
        """), SpriteKind.player)

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
        """), SpriteKind.enemy)

    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.max = 50
    statusbar2.value = 50
    statusbar2.set_label("dragon HP", 15)
    statusbar2.set_position(116, 70)

    statusbar = statusbars.create(20, 4, StatusBarKind.health)
    statusbar.attach_to_sprite(mySprite)
    statusbar.set_label("your HP", 15)
    statusbar.max = 100
    statusbar.value = 100
    statusbar.set_position(122, 60)
    
    currentStage = 0 # Set stage to Level 1

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

    scene.set_background_color(5) # Change background color for new level
    
    textSprite4 = textsprite.create("level #2 select an action", 1, 15)
    textSprite5 = textsprite.create("<A> = Basic attack", 1, 15)
    textSprite6 = textsprite.create("<B> = shield", 1, 15)
    textSprite7 = textsprite.create("<UP> = strong attack", 1, 15)
    
    textSprite4.set_position(80, 10)
    textSprite5.set_position(60, 30)
    textSprite6.set_position(42, 40)
    textSprite7.set_position(55, 50)

    # Setup new enemy for level 2
    mySprite2 = sprites.create(img("""
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        2 2 2 2 2 2 2 2 2 2 2 2 2 2 2 2
        """), SpriteKind.enemy)
    
    # Create new status bar for level 2 enemy (Goblin King)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.enemy_health)
    statusbar2.attach_to_sprite(mySprite2)
    statusbar2.max = 80 # Harder boss
    statusbar2.value = 80
    statusbar2.set_label("Goblin HP", 15)
    statusbar2.set_position(116, 70)
    
    currentStage = 1 # Set stage to Level 2

# Handler to check for level changes every 100ms
def on_update_interval():
    global currentStage
    if currentStage == 0 and statusbar2.value <= 0:
        game.splash("Dragon Defeated!", "Proceed to Level 2!")
        setupLevel2()
    elif currentStage == 1 and statusbar2.value <= 0:
        game.over(True, effects.confetti)
game.on_update_interval(100, on_update_interval)

# --- Input Handlers (Modified to check current stage) ---

def on_a_pressed():
    if currentStage == 0 or currentStage == 1:
        statusbar2.value += -10
        game.splash("you did -10 HP to enemy")
        # Simplified enemy retaliation logic
        damageTaken = randint(0, 10)
        game.splash("you took -" + str(damageTaken) + " HP")
        statusbar.value += -damageTaken
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_b_pressed():
    if currentStage == 0 or currentStage == 1:
        damageBlocked = randint(0, 5)
        if damageBlocked == 0:
            game.splash("You blocked all damage!")
        else:
            game.splash("You blocked some damage, took -" + str(damageBlocked) + " HP")
            statusbar.value += -damageBlocked
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# New move for Level 2
def on_up_pressed():
    if currentStage == 1:
        statusbar2.value += -20
        game.splash("Strong attack! -20 HP to Goblin King!")
        # Enemy retaliates less harshly after strong attack
        damageTaken = randint(0, 5)
        game.splash("you took -" + str(damageTaken) + " HP")
        statusbar.value += -damageTaken
    elif currentStage == 0:
        game.splash("Strong attack not unlocked yet!")
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)


# Global variable initialization (must be done outside functions if used globally)
textSprite3: TextSprite = None
textSprite2: TextSprite = None
textSprite: TextSprite = None
textSprite7: TextSprite = None
textSprite6: TextSprite = None
textSprite5: TextSprite = None
textSprite4: TextSprite = None
mySprite: Sprite = None
statusbar: StatusBarSprite = None
mySprite2: Sprite = None
statusbar2: StatusBarSprite = None

# Start the game at Level 1
setupLevel1()
