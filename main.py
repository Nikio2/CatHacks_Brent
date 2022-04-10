import winsound
from random import randint

from graphics import *


def useless():
    # set up the background
    width = 1080
    height = 720
    win = GraphWin('Useful Hack', width, height, autoflush=False)
    win.setCoords(0, 0, 1080, 720)
    win.setBackground("black")

    # read in text file
    fact_file = open('Useless_Facts.txt', encoding="utf8")
    lines = fact_file.readlines()

    # Start Box
    Start = Rectangle(Point(width / 2 - 200, height / 2 - 100), Point(width / 2 + 200, height / 2 + 100))
    Start.setOutline("white")
    Start.draw(win)

    # Start Message
    Start_message = Text(Point(width / 2, height / 2), "Press to Start")
    Start_message.setFace("courier")
    Start_message.setSize(20)
    Start_message.setTextColor("white")
    Start_message.draw(win)

    # Welcome Message
    Welcome_image = Image(Point(width / 2, (height / 2 + 100+720)/2), "Title_image.gif").draw(win)

    # Music Files
    startup_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\sm64_here_we_go.wav'
    start_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\sm64_mario_press_start.wav'
    click_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\sm64_enter_course.wav'
    impact_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\sm64_impact.wav'
    warp_zone_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\Mario_Underworld.wav'
    coin_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\smb_coin.wav'
    jump_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\smb_jump-super.wav'
    pipe_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\nsmb_pipe.wav'
    game_over_file = 'C:\\Users\\brent\\Desktop\\CatHacks\\smas-smb3_game_over.wav'

    winsound.PlaySound(startup_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_NOSTOP)
    # Do the stars
    # Mario Figure
    mario = Image(Point(950, 90), "mario.gif")
    luigi = Image(Point(50, 90), "luigi.gif")
    mario.draw(win)
    luigi.draw(win)
    i=0
    c=0
    while i < 64:
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        win.plot(randint(0, 1080), randint(0, 720), "white")
        if i <= 12:
            mario.move(-30, 0)
            luigi.move(28, 0)

            update(5)
        elif i <= 18:
            mario.move(0, 20)
            if c==0:
                mario.move(0, 20)
                c+=1
            luigi.move(30, 0)
            update(5)
        elif i <= 25:
            if i == 20:
                winsound.PlaySound(coin_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
            mario.move(0, -20)
            luigi.move(20, 0)

            update(5)
        elif i <= 38:
            mario.move(-20, 0)
            luigi.move(10, 0)
            update(5)
        i+=1
    winsound.PlaySound(start_file, winsound.SND_FILENAME)

    win.getMouse()
    Start_message.undraw()
    winsound.PlaySound(click_file, winsound.SND_FILENAME)
    Start.undraw()
    Welcome_image.undraw()
    mario.undraw()
    luigi.undraw()
    background = Image(Point(width / 2, height / 2), "Warped.gif").draw(win)

    # platform
    platform = Image(Point(740, 340), "Platform.gif").draw(win)

    # Level text
    level = Image(Point(width/2, height/2 + 100), "Text.gif").draw(win)
    # (820, 650) the point in which Mario starts on the landed platform
    # (820, 750) is where he starts off of screen.
    m_w = mario.getWidth()
    m_h = mario.getHeight()
    m_w = 590 - m_w
    m_h = 740 - m_h
    mario.move(m_w, m_h)
    mario.draw(win)

    for i in range(4):
        mario.move(0, -25)
        update(4)
    winsound.PlaySound(impact_file, winsound.SND_FILENAME)
    winsound.PlaySound(warp_zone_file, winsound.SND_FILENAME | winsound.SND_ASYNC | winsound.SND_LOOP)
    win.getMouse()
    level.undraw()

    for i in range(4):
        mario.move(-20, 0)
        update(4)
    for i in range(5):
        mario.move(0, -50)
        update(4)

    level_select = win.getMouse()
    if level_select.getX() >= (630):
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(-20, 0)
            update(4)
        for i in range(3):
            mario.move(0, -20)
            update(4)
        mario.move(0, -10)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        pipe = Image(Point((m_w+130), m_h-430), "pipe2.gif").draw(win)

        for i in range(4):
            if i == 1:
                winsound.PlaySound(pipe_file, winsound.SND_FILENAME)
            mario.move(0, -20)
            update(4)
    elif 450 < level_select.getX() < 630:
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(-20, 0)
            update(4)
        for i in range(3):
            mario.move(0, -20)
            update(4)
        mario.move(0, -10)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        update(5)
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(0, 10)
            mario.move(-20, 0)
            update(4)

        for i in range(4):
            mario.move(0, -10)
            mario.move(-20, 0)
            update(4)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        pipe = Image(Point((m_w-33), m_h-430), "pipe2.gif").draw(win)
        for i in range(4):
            if i == 1:
                winsound.PlaySound(pipe_file, winsound.SND_FILENAME)
            mario.move(0, -20)
            update(4)
    elif level_select.getX() <= 450:
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(-20, 0)
            update(4)
        for i in range(3):
            mario.move(0, -20)
            update(4)
        mario.move(0, -10)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        update(5)
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(0, 10)
            mario.move(-20, 0)
            update(4)

        for i in range(4):
            mario.move(0, -10)
            mario.move(-20, 0)
            update(4)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        update(5)
        winsound.PlaySound(jump_file, winsound.SND_FILENAME | winsound.SND_ASYNC)
        for i in range(4):
            mario.move(0, 10)
            mario.move(-20, 0)
            update(4)

        for i in range(4):
            mario.move(0, -10)
            mario.move(-20, 0)
            update(4)
        winsound.PlaySound(impact_file, winsound.SND_FILENAME)
        pipe = Image(Point((m_w-20)-170, m_h-430), "pipe2.gif").draw(win)
        for i in range(4):
            if i == 1:
                winsound.PlaySound(pipe_file, winsound.SND_FILENAME)
            mario.move(0, -20)
            update(4)

    text = Image(Point(width / 2 - 30, height / 2 + 100), "text2.gif").draw(win)

    win.getMouse()
    text.undraw()
    mario.undraw()
    pipe.undraw()
    background.undraw()
    platform.undraw()
    win.setBackground("black")
    mario2 = Image(Point(820, 750), "mario.gif").draw(win)

    for i in range(10):
        mario2.move(0, -50)
        update(4)
    winsound.PlaySound(impact_file, winsound.SND_FILENAME)

    lakitu = Image(Point(width/4, height-300), "lakitu.gif").draw(win)

    Game_Over_Message = Text(Point(width / 3 + 100, height - 50), "Mario, Peach is fine go home. Ooh, but did you know...")
    Game_Over_Message.setFace("courier")
    Game_Over_Message.setSize(15)
    Game_Over_Message.setTextColor("white")
    Game_Over_Message.draw(win)

    Game_Over_Message2 = Text(Point(width/3 + 150, height-100), lines[randint(1,731)])
    Game_Over_Message2.setFace("courier")
    Game_Over_Message2.setSize(12)
    Game_Over_Message2.setTextColor("white")
    Game_Over_Message2.draw(win)

    winsound.PlaySound(game_over_file, winsound.SND_FILENAME)

    for i in range(75):
        print("")
        update(5)
    for i in range(10):
        mario2.move(0, -50)
        update(9)

    game_over = Image(Point(width/2, 355), "game-over.gif").draw(win)
    win.getMouse()
    win.close()


useless()