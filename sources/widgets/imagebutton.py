from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior


class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)
