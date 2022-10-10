def get_area(file_name):
    import pygame as pg

    original = pg.image.load(file_name)

    MAX_WIDTH = 1300
    MAX_HEIGHT = 700

    WIDTH = MAX_WIDTH if original.get_width() >= MAX_WIDTH else original.get_width()
    HEIGHT = MAX_HEIGHT if original.get_width() >= MAX_HEIGHT else original.get_height()

    pg.init()
    clock = pg.time.Clock()
    sc = pg.display.set_mode((WIDTH, HEIGHT))

    area = pg.Surface(original.get_size()).convert_alpha()
    area.fill((0, 0, 0, 0))

    d1 = WIDTH/original.get_width()
    d2 = HEIGHT/original.get_height()
    r = min(original.get_size())//10
    img = pg.transform.scale(original, (WIDTH, HEIGHT))

    running = True
    mouse = [False, False]
    mPos = pg.mouse.get_pos()
    while running:
        mPos = pg.mouse.get_pos()
        sc.fill((0,)*3)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse[0] = True
                if event.button == 3:
                    mouse[1] = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    mouse[0] = False
                if event.button == 3:
                    mouse[1] = False

        if mouse[0]:
            pg.draw.circle(area, (0, 0, 255, 100), (mPos[0] / d1, mPos[1] / d2), r)
        if mouse[1]:
            pg.draw.circle(area, (0, 0, 0, 0), (mPos[0] / d1, mPos[1] / d2), r)

        sc.blit(img, (0, 0))
        barea = pg.transform.scale(area, (WIDTH, HEIGHT))
        sc.blit(barea, (0, 0))

        pg.display.update()
        clock.tick(-1)

    ret = pg.Surface(original.get_size())
    for x in range(ret.get_width()):
        for y in range(ret.get_height()):
            if area.get_at((x, y)) == (0, 0, 255, 100):
                ret.set_at((x, y), original.get_at((x, y)))

    pg.quit()
    return ret