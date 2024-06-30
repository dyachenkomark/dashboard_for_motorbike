from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

Builder.load_file('sources/widgets/speedometerview.kv')


class SpeedometerView(FloatLayout):
    anim = None

    def set_speed_value(self, value):
        self.anim = Animation(value=value, max=max(self.max, value), d=0.2)
        self.anim.start(self)
        # self.sp_val = value
        # self.sp_max = max(value, self.sp_max)

    def reset_max_speed(self):
        self.max = 0.0

    def __init__(self, **kwargs):
        super(SpeedometerView, self).__init__(**kwargs)



