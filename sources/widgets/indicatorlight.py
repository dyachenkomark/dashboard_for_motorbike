from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.properties import NumericProperty

indicatorlight_layout = '''
<IndicatorLight>:
    Image:
        id: side
        source: 'images/Light_Side.png'
        opacity: 1.0 if root.value == 1 else 0.0
    Image:
        id: close
        source: 'images/Light_Close.png'
        opacity: 1.0 if root.value == 2 else 0.0
    Image:
        id: far
        source: 'images/Light_Far.png'
        opacity: 1.0 if root.value == 3 else 0.0
'''

Builder.load_string(indicatorlight_layout)


class IndicatorLight(AnchorLayout):
    anchor_x = 'center'
    anchor_y = 'center'

    OFF = 0
    SIDE = 1
    CLOSE = 2
    FAR = 3

    value = NumericProperty(0)

    def __init__(self, **kwargs):
        super(IndicatorLight, self).__init__(**kwargs)

    def set(self, value):
        self.value = value
