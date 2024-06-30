from kivy.uix.screenmanager import ScreenManager, SlideTransition
from sources.mainscreen import MainScreen
from sources.flagsscreen import FlagsScreen
from sources.consolescreen import ConsoleScreen
from sources.mapscreen import MapScreen


class Dashboard(ScreenManager):
    def __init__(self, **kwargs):
        self.transition = SlideTransition()
        super(Dashboard, self).__init__(**kwargs)
        
        self.mainscreen = MainScreen(name='main')
        self.flagsscreen = FlagsScreen(name='flags')
        self.consolescreen = ConsoleScreen(name='console')
        self.mapscreen = MapScreen(name='map')

        self.add_widget(self.mainscreen)
        self.add_widget(self.flagsscreen)
        self.add_widget(self.consolescreen)
        self.add_widget(self.mapscreen)

        self.indicator_light = self.mainscreen.ids.light
        self.tl_left = self.mainscreen.ids.tl_left
        self.tl_right = self.mainscreen.ids.tl_right
        self.indicator_speed = self.mainscreen.ids.speed
        self.indicator_current = self.mainscreen.ids.current
        self.indicator_footstep = self.mainscreen.ids.footstep


