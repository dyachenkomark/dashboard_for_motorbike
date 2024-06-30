from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.animation import Animation

Builder.load_file('sources/widgets/currentview.kv')


class CurrentView(FloatLayout):
    anim = None

    def __init__(self, **kwargs):
        super(CurrentView, self).__init__(**kwargs)

    def set_current_value(self, value):
        self.anim = Animation(value=value, d=0.2)
        self.anim.start(self)
