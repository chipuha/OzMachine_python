import pygame as pg
import pygame.gfxdraw as gfxdraw
import numpy as np
import load_art as art


class Button:
    def __init__(self, surface_location, x, y, width, height, text=''):
        self.surface_location = surface_location
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, screen, selected_lith=''):
        image_map = {
            'Unknown': art.UnknownBtnIMG, 'Halite': art.HaliteBtnIMG, 'Gypsum': art.GypsumBtnIMG,
            'Anhydrite': art.AnhydriteBtnIMG, 'Dolomite': art.DolomiteBtnIMG, 'Dolomitic LS': art.DolomiticLSBtnIMG,
            'Cherty Dol LS': art.ChertyDolLSBtnIMG, 'Cherty Dol': art.ChertyDolBtnIMG, 'Limestone': art.LimestoneBtnIMG,
            'Cherty LS': art.ChertyLSBtnIMG, 'Chert': art.ChertBtnIMG, 'Shale': art.ShaleBtnIMG,
            'Sandstone': art.SandstoneBtnIMG, 'Ironstone': art.IronstoneBtnIMG, 'Coal': art.CoalBtnIMG
        }
        font = pg.font.SysFont('georgia', 12)

        if self.text in image_map:
            if selected_lith == self.text:
                pg.draw.rect(screen, art.RED, (self.x - 2.5, self.y - 2.5, self.width + 6, self.height + 6), 0)
                pg.draw.rect(screen, art.WHITE, (self.x, self.y, self.width, self.height), 0)

                img_border = (self.width - 72) / 2
                screen.blit(image_map[self.text], (self.x + img_border, self.y + img_border))

                text = font.render(self.text, True, art.BLACK)
                txt_border = self.height - img_border - text.get_height()
                screen.blit(text, (self.x + round((self.width / 2 - text.get_width() / 2)),
                                   self.y + txt_border))

            else:
                pg.draw.rect(screen, art.BLACK, (self.x - 2.5, self.y - 2.5, self.width + 6, self.height + 6), 0)
                pg.draw.rect(screen, art.WHITE, (self.x, self.y, self.width, self.height), 0)

                img_border = (self.width - 72) / 2
                screen.blit(image_map[self.text], (self.x + img_border, self.y + img_border))

                text = font.render(self.text, True, art.BLACK)
                txt_border = self.height - img_border - text.get_height()
                screen.blit(text, (self.x + round((self.width / 2 - text.get_width() / 2)),
                                   self.y + txt_border))

        else:
            pg.draw.rect(screen, art.BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            pg.draw.rect(screen, art.WHITE, (self.x, self.y, self.width, self.height), 0)
            text = font.render(self.text, True, art.BLACK)
            screen.blit(text, (self.x + round((self.width / 2 - text.get_width() / 2)),
                               self.y + round((self.height / 2 - text.get_height() / 2))))

    def selected(self, pos):
        if self.x + self.surface_location[0] < pos[0] < self.x + self.surface_location[0] + self.width:
            if self.y + self.surface_location[1] < pos[1] < self.y + self.surface_location[1] + self.height:
                return True
        return False


class OnOffButton:
    def __init__(self, surface_location, x, y, width, height, text, status):
        self.surface_location = surface_location
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.status = status

    def draw(self, screen):
        font = pg.font.SysFont('georgia', 12)
        if self.status:
            pg.draw.rect(screen, art.BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            pg.draw.rect(screen, art.LIGHT_GREEN, (self.x, self.y, self.width, self.height), 0)
            text = font.render(self.text, True, art.BLACK)
            screen.blit(text, (self.x + round((self.width / 2 - text.get_width() / 2)),
                               self.y + round((self.height / 2 - text.get_height() / 2))))
        else:
            pg.draw.rect(screen, art.BLACK, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)
            pg.draw.rect(screen, art.WHITE, (self.x, self.y, self.width, self.height), 0)
            text = font.render(self.text, True, art.BLACK)
            screen.blit(text, (self.x + round((self.width / 2 - text.get_width() / 2)),
                               self.y + round((self.height / 2 - text.get_height() / 2))))

    def selected(self, pos):
        if self.x + self.surface_location[0] < pos[0] < self.x + self.surface_location[0] + self.width:
            if self.y + self.surface_location[1] < pos[1] < self.y + self.surface_location[1] + self.width:
                if not self.status:
                    self.status = True
                else:
                    self.status = False


class LithButton:
    def __init__(self, surface_location, x, y, width, height):
        self.surface_location = surface_location
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.lith_status = 'Unknown'

    def selected(self, pos, lith_status):
        if self.x + self.surface_location[0] <= pos[0] <= self.x + self.surface_location[0] + self.width:
            if self.y + self.surface_location[1] < pos[1] <= self.y + self.surface_location[1] + self.height:
                if self.lith_status == lith_status:
                    self.lith_status = 'Unknown'
                else:
                    self.lith_status = lith_status
                return True


def draw_grid(screen, n_blocks_tall, n_blocks_wide):
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    x_block_size = screen_width / n_blocks_wide
    y_block_size = screen_height / n_blocks_tall
    for y in range(n_blocks_tall):
        if y % 5 == 0:
            pg.draw.line(screen, art.LIGHT_BLUE, (0, y * y_block_size), (screen_width, y * y_block_size), 2)
        else:
            pg.draw.line(screen, art.LIGHT_BLUE, (0, y * y_block_size), (screen_width, y * y_block_size), 1)
    for x in range(n_blocks_wide):
        if x % 5 == 0:
            pg.draw.line(screen, art.LIGHT_BLUE, (x * x_block_size, 0), (x * x_block_size, screen_height), 2)
        else:
            pg.draw.line(screen, art.LIGHT_BLUE, (x * x_block_size, 0), (x * x_block_size, screen_height), 1)


def draw_depth(screen, n_blocks_tall, depths):
    n_sections_tall = int(n_blocks_tall / 5)
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    y_block_size = screen_height / n_sections_tall

    font = pg.font.SysFont('georgia', 12)
    for y in range(len(depths)):
        if y == 0:
            # draw the text "Depth" at the top
            text = font.render(depths[y], True, art.BLACK, [255, 255, 255])
            screen.blit(text, (screen_width / 2 - 25, y))  # could center text better
        else:
            # draw marker lines on either side of depth value
            pg.draw.line(screen, art.BLACK, (0, y * y_block_size), (10, y * y_block_size), 1)
            pg.draw.line(screen, art.BLACK, (screen_width - 10, y * y_block_size), (screen_width, y * y_block_size), 1)
            # draw the depth value
            text = font.render(str(depths[y]), True, art.BLACK, [255, 255, 255])
            screen.blit(text, (screen_width / 2 - 13, y * y_block_size - 7))  # could center text better


def draw_log(screen, whole_log, color, scale, wrapping, wrap_color=art.BLUE):
    wrap_color += (100,)
    log_lines, log_polygons = normalize_log_to_screen(whole_log, screen, scale, wrapping)

    if wrapping:

        for log in log_polygons:
            pg.draw.aalines(screen, color, True, log, 1)
            pg.gfxdraw.filled_polygon(screen, log, wrap_color)

    for log in log_lines:
        pg.draw.aalines(screen, color, False, log, 1)


def normalize_log_to_screen(log, screen, scale, wrapping):
    delta_new = scale[1] - scale[0]
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    y_values = list(np.linspace(0, screen_height, len(log)))
    if wrapping:
        without_wrapping = [int((x - scale[0]) / scale[1] * (screen_width / delta_new * scale[1])) for x in log]
        points = list(zip(without_wrapping, y_values))
        return log_wrapping(points, screen_width)
    else:
        x_values = [int((screen_width / delta_new) * x) for x in log]
        return [list(zip(x_values, y_values))], None


def log_wrapping(log, maximum):
    polygons = []
    lines = []

    above_max = []
    middle = []
    below_zero = []
    y = 0
    for x, y in log:
        if x < 0:
            below_zero.append((x, y))
            if middle:  # make sure a has something in it
                middle.append((0, y))
                lines.append(middle)
            if above_max:  # make sure a has something in it
                above_max_t = [(x - maximum, y) for x, y in above_max]
                above_max_t.insert(0, (0, above_max_t[0][1]))
                above_max_t.append((0, above_max_t[-1][1]))
                polygons.append(above_max_t)
            middle = []
            above_max = []
        elif x > maximum:
            above_max.append((x, y))
            if middle:  # make sure a has something in it
                middle.append((maximum, y))
                lines.append(middle)
            if below_zero:  # make sure a has something in it
                below_zero_t = [(x + maximum, y) for x, y in below_zero]
                below_zero_t.insert(0, (maximum, below_zero_t[0][1]))
                below_zero_t.append((maximum, below_zero_t[-1][1]))
                polygons.append(below_zero_t)
            middle = []
            below_zero = []
        else:
            if above_max:  # make sure a has something in it
                middle.append((maximum, y))
                above_max_t = [(x - maximum, y) for x, y in above_max]
                above_max_t.insert(0, (0, above_max_t[0][1]))
                above_max_t.append((0, above_max_t[-1][1]))
                polygons.append(above_max_t)
            if below_zero:  # make sure a has something in it
                middle.append((0, y))
                below_zero_t = [(x + maximum, y) for x, y in below_zero]
                below_zero_t.insert(0, (maximum, below_zero_t[0][1]))
                below_zero_t.append((maximum, below_zero_t[-1][1]))
                polygons.append(below_zero_t)
            middle.append((x, y))
            below_zero = []
            above_max = []

    if middle:  # make sure a has something in it
        if len(middle) < 2:
            middle.append((middle[0][0], y))
        lines.append(middle)
    if above_max:  # make sure a has something in it
        above_max_t = [(x - maximum, y) for x, y in above_max]
        above_max_t.insert(0, (0, above_max_t[0][1]))
        above_max_t.append((0, above_max_t[-1][1]))
        polygons.append(above_max_t)
    if below_zero:  # make sure a has something in it
        below_zero_t = [(x + maximum, y) for x, y in below_zero]
        below_zero_t.insert(0, (maximum, below_zero_t[0][1]))
        below_zero_t.append((maximum, below_zero_t[-1][1]))
        polygons.append(below_zero_t)

    return lines, polygons


def draw_track(screen, log_info, surface_size, surface_location, track_number):
    track = pg.Surface(surface_size)
    track.fill(art.WHITE)
    # draw grid
    draw_grid(track, log_info.n_zones, 10)

    if track_number == 1:
        # draw gamma ray log
        draw_log(track, log_info.logs['GR'], art.BLACK, (0, 150), False)
        # # draw boarder
        pg.draw.rect(track, art.BLACK, [0, 0, surface_size[0], surface_size[1]], 1)
        # display track
        screen.blit(track, surface_location)

    elif track_number == 3:
        # draw neutron porosity log
        draw_log(track, log_info.logs['NPHI'], art.BLACK, (30, -10), True, art.LIGHT_GREY)
        # draw density porosity log
        draw_log(track, log_info.logs['DPHI'], art.GREEN, (30, -10), True, art.LIGHT_GREEN)
        # draw Pe log
        draw_log(track, log_info.logs['PE'], art.RED, (0, 20), False)
        # draw border
        pg.draw.rect(track, art.BLACK, [0, 0, surface_size[0], surface_size[1]], 1)
        # display track
        screen.blit(track, surface_location)
