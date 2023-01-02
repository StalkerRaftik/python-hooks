from hooks import Hooks


HOOKS = Hooks()


class Color:
    __slots__ = ('r', 'g', 'b')

    def __init__(self, r: int, g: int, b: int):
        self.r = r
        self.g = g
        self.b = b

    def __repr__(self):
        return f'Color({self.r}, {self.g}, {self.b})'


class Screen:
    def __init__(self, x: int, y: int):
        self.screen = [
            [Color(255, 255, 255) for _ in range(y)]
            for _ in range(x)
        ]

    def draw_tick(self):
        HOOKS.call('pre_draw_tick', self.screen)
        print('Screen rendering....')
        self.screen[0][0] = Color(0, 0, 0)
        HOOKS.call('post_draw_tick', self.screen)


class Logger:
    def __init__(self):
        HOOKS.add('pre_draw_tick', 'log_screen_data', self.log_pre_draw)
        HOOKS.add('post_draw_tick', 'log_screen_data', self.log_post_draw)

    @staticmethod
    def log_pre_draw(screen):
        print('Logging pre-draw screen data...', screen[0][0], sep='\n')

    @staticmethod
    def log_post_draw(screen):
        print('Logging post-draw screen data...', screen[0][0], sep='\n')


scr = Screen(10, 10)
logger = Logger()
scr.draw_tick()
