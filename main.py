import pygame as pg
import random
from OzMachine_python.ui_tools import Button, OnOffButton, LithButton, draw_depth, draw_track
import OzMachine_python.load_art as art
from OzMachine_python.log_handler import LogHandler


pg.init()
screen = pg.display.set_mode([1045, 750])
font = pg.font.SysFont('georgia', 12)
header_font = pg.font.SysFont('georgia', 20)


def game():
    # load logs and lithology
    log_info = LogHandler()

    # game parameters and initial settings
    clock = pg.time.Clock()

    done = False
    selected_user_lith = "Unknown"

    # start drawing
    # Fill the background with DARK GREY
    screen.fill(art.DARK_GREY)

    # draw chart background
    pg.draw.rect(screen, art.GREY, [20, 20, 685, 710], 0)

    # draw log chart
    # background
    pg.draw.rect(screen, art.WHITE, [40, 40, 645, 670], 0)

    well_names = ['BLUE MAVERICK 34-1', 'BIG CRAWDAD 25-3-34', 'BIG MONEY HONEY 6-43-5H',
                  'BEANS STATION 15-8-1H', 'AUNT MABEL 25-9-23', 'LIONS GRASP 4-32-50', 'BOBS COUCH 10-5-23 4',
                  'PETERSON RANCH 4-25-3 1H', 'BLACK GOLD 2-45', 'FINGERS CROSSED 9-12', ]
    # draw well name and info
    header_text = header_font.render(well_names[random.randint(0, 9)], True, art.BLACK)
    screen.blit(header_text, (int(370 - (.5 * header_text.get_rect().width)), 60))

    # log labels and scale
    gr_text = font.render('0  ——  Gamma Ray (API)  ——  150', True, art.BLACK)
    pe_text = font.render('0 ———— Pe (barns/e)   ————  10', True, art.RED)
    dp_text = font.render('30  ————-———  Density Porosity (ls eq. units)   ————————  -10', True, art.GREEN)
    np_text = font.render('30  ————-———  Neutron Porosity (ls eq. units)  ————————  -10', True, art.BLACK)

    # track 1 (Gamma Ray)
    #
    track1_surface_size = (180, 500)
    track1_surface_location = (60, 190)

    # draw log label and scale
    screen.blit(gr_text, (track1_surface_location[0]-3, track1_surface_location[1]-25))

    # draw the track surface
    draw_track(screen, log_info, track1_surface_size, track1_surface_location, 1)

    # track 2 (Depth)
    #
    track2_surface_size = (65, 500)
    track2_surface_location = (240, 190)
    track2 = pg.Surface(track2_surface_size)
    track2.fill(art.WHITE)

    # draw depth values and markers
    draw_depth(track2, log_info.n_zones, log_info.logs['DEPTH'])
    screen.blit(track2, track2_surface_location)

    # track 3 (PE, Density, Neutron)
    #
    track3_surface_size = (360, 500)
    track3_surface_location = (305, 190)

    # draw log label and scale
    screen.blit(pe_text, (track3_surface_location[0]-3, track3_surface_location[1] - 75))
    screen.blit(dp_text, (track3_surface_location[0]-3, track3_surface_location[1] - 50))
    screen.blit(np_text, (track3_surface_location[0]-3, track3_surface_location[1] - 25))

    # draw the track surface
    draw_track(screen, log_info, track3_surface_size, track3_surface_location, 3)

    # create buttons
    # depth track lith buttons
    lith_buttons = []
    for x in range(0, log_info.n_zones):
        height = track2_surface_size[1] / log_info.n_zones
        lith_buttons.append(LithButton(track2_surface_location, 0, int(x * height), track2_surface_size[0], height))

    # button screen
    buttons_surface = pg.Surface((300, 710))
    buttons_surface_location = (725, 20)
    buttons_surface.fill(art.GREY)

    # create user lith buttons
    halite_button = Button(buttons_surface_location, 20, 105, 80, 50, 'Halite')
    gypsum_button = Button(buttons_surface_location, 110, 105, 80, 50, 'Gypsum')
    anhydrite_button = Button(buttons_surface_location, 200, 105, 80, 50, 'Anhydrite')
    dolomite_button = Button(buttons_surface_location, 110, 165, 80, 50, 'Dolomite')
    dolomitcls_button = Button(buttons_surface_location, 20, 225, 80, 50, 'Dolomitic LS')
    chertydolls_button = Button(buttons_surface_location, 110, 225, 80, 50, 'Cherty Dol LS')
    chertydol_button = Button(buttons_surface_location, 200, 225, 80, 50, 'Cherty Dol')
    limestone_button = Button(buttons_surface_location, 20, 285, 80, 50, 'Limestone')
    chertyls_button = Button(buttons_surface_location, 110, 285, 80, 50, 'Cherty LS')
    chert_button = Button(buttons_surface_location, 200, 285, 80, 50, 'Chert')
    shale_button = Button(buttons_surface_location, 110, 345, 80, 50, 'Shale')
    sandstone_button = Button(buttons_surface_location, 20, 405, 80, 50, 'Sandstone')
    ironstone_button = Button(buttons_surface_location, 110, 405, 80, 50, 'Ironstone')
    coal_button = Button(buttons_surface_location, 200, 405, 80, 50, 'Coal')
    newlognolith_button = Button(buttons_surface_location, 75, 485, 150, 30, 'New log without lithology')
    newloglith_button = Button(buttons_surface_location, 75, 525, 150, 30, 'New log with lithology')
    checklith_button = OnOffButton(buttons_surface_location, 75, 565, 150, 30, 'Check lithology', False)

    pg.display.update()

    while not done:

        # draw user lith buttons
        halite_button.draw(buttons_surface, selected_user_lith)
        gypsum_button.draw(buttons_surface, selected_user_lith)
        anhydrite_button.draw(buttons_surface, selected_user_lith)
        dolomite_button.draw(buttons_surface, selected_user_lith)
        dolomitcls_button.draw(buttons_surface, selected_user_lith)
        chertydolls_button.draw(buttons_surface, selected_user_lith)
        chertydol_button.draw(buttons_surface, selected_user_lith)
        limestone_button.draw(buttons_surface, selected_user_lith)
        chertyls_button.draw(buttons_surface, selected_user_lith)
        chert_button.draw(buttons_surface, selected_user_lith)
        shale_button.draw(buttons_surface, selected_user_lith)
        sandstone_button.draw(buttons_surface, selected_user_lith)
        ironstone_button.draw(buttons_surface, selected_user_lith)
        coal_button.draw(buttons_surface, selected_user_lith)
        newlognolith_button.draw(buttons_surface)
        newloglith_button.draw(buttons_surface)
        checklith_button.draw(buttons_surface)

        # check for button clicks
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:

                if halite_button.selected(event.pos):
                    selected_user_lith = 'Halite'
                    break
                if gypsum_button.selected(event.pos):
                    selected_user_lith = "Gypsum"
                    break
                if anhydrite_button.selected(event.pos):
                    selected_user_lith = "Anhydrite"
                    break
                if dolomite_button.selected(event.pos):
                    selected_user_lith = "Dolomite"
                    break
                if dolomitcls_button.selected(event.pos):
                    selected_user_lith = "Dolomitic LS"
                    break
                if chertydolls_button.selected(event.pos):
                    selected_user_lith = "Cherty Dol LS"
                    break
                if chertydol_button.selected(event.pos):
                    selected_user_lith = "Cherty Dol"
                    break
                if limestone_button.selected(event.pos):
                    selected_user_lith = "Limestone"
                    break
                if chertyls_button.selected(event.pos):
                    selected_user_lith = "Cherty LS"
                    break
                if chert_button.selected(event.pos):
                    selected_user_lith = "Chert"
                    break
                if shale_button.selected(event.pos):
                    selected_user_lith = "Shale"
                    break
                if sandstone_button.selected(event.pos):
                    selected_user_lith = "Sandstone"
                    break
                if ironstone_button.selected(event.pos):
                    selected_user_lith = "Ironstone"
                    break
                if coal_button.selected(event.pos):
                    selected_user_lith = "Coal"
                    break
                if newlognolith_button.selected(event.pos):
                    log_info = LogHandler()
                    draw_track(screen, log_info, track1_surface_size, track1_surface_location, 1)
                    draw_track(screen, log_info, track3_surface_size, track3_surface_location, 3)
                    track2.fill(art.WHITE)
                    draw_depth(track2, log_info.n_zones, log_info.logs['DEPTH'])
                    for button in lith_buttons:
                        button.lith_status = 'Unknown'
                    break
                if newloglith_button.selected(event.pos):
                    log_info = LogHandler()
                    draw_track(screen, log_info, track1_surface_size, track1_surface_location, 1)
                    draw_track(screen, log_info, track3_surface_size, track3_surface_location, 3)
                    for i, button in enumerate(lith_buttons):
                        button.lith_status = log_info.get_lith(log_info.true_lith[i])
                        track2.blit(log_info.get_lith_art(button.lith_status), (button.x, button.y))
                    draw_depth(track2, log_info.n_zones, log_info.logs['DEPTH'])
                    break

                checklith_button.selected(event.pos)

                # draw lith buttons
                for button in lith_buttons:
                    if button.selected(event.pos, selected_user_lith):
                        for button_2 in lith_buttons:
                            track2.blit(log_info.get_lith_art(button_2.lith_status), (button_2.x, button_2.y))
                        draw_depth(track2, log_info.n_zones, log_info.logs['DEPTH'])
                        break

        if checklith_button.status:
            text = font.render('x', True, art.RED)
            for i, button in enumerate(lith_buttons):
                if button.lith_status != 'Unknown':
                    if log_info.get_lith(button.lith_status) != int(log_info.true_lith[i]):
                        track2.blit(text, (button.x+3, button.y-2))

        screen.blit(track2, track2_surface_location)
        screen.blit(buttons_surface, buttons_surface_location)

        pg.display.update()
        clock.tick(30)


game()
pg.quit()
