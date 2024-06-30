from kivy.uix.screenmanager import Screen
from kivy.animation import Animation
from kivy.lang import Builder

mainscreen_layout = '''
#:import SpeedometerView sources.widgets.speedometerview
#:import CurrentView sources.widgets.currentview
#:import IndicatorLight sources.widgets.indicatorlight
#:import ModeView sources.widgets.modeview
#:import TurnLight sources.widgets.turnlight


<MainScreen>:
    name: 'Dashboard' 
    BoxLayout:
        orientation: 'vertical'
        BoxLayout:
            size_hint: 1.0, 0.1
            Button:
                font_size: 30
                text: 'FLAGS'
                on_release: app.root.current = 'flags'
            Button:
                font_size: 30
                text: 'BATTERY'
            Button:
                font_size: 30
                text: 'MAP'
                on_release: app.root.current = 'map'
        FloatLayout:
            BoxLayout
                orientation: 'horizontal'
                SpeedometerView:
                    id: speed
                CurrentView:
                    id: current
            AnchorLayout:
                anchor_x: 'center'
                anchor_y: 'center'
                BoxLayout:
                    orientation: 'vertical'
                    size_hint: 1, 1
                    Widget
                        size_hint: 1, 1
                    ModeView:
                        id: mode
                    IndicatorLight:
                        id: light
                    Label:
                        id: footstep
                        text: 'FOOTSTEP'
                        font: 'fonts/SysBoldItalic.ttf'
                        font_size: 40
                        color: 1,0,0,1
                        opacity: 0.0
    
            BoxLayout
                orientation: 'horizontal'
                TurnLight:
                    id: tl_left
                    direction: 'left'
                Widget
                TurnLight:
                    id: tl_right
                    direction: 'right'
            
    Image:
        id: logo
        source: 'images/Logo_RUDN.png'
'''

Builder.load_string(mainscreen_layout)


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        logo = self.ids.logo
        anim = Animation(opacity=1.0, d=1) + Animation(opacity=0.0, d=1.5)
        anim.start(logo)
