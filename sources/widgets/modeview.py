from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from sources.widgets.imagebutton import ImageButton

from kivy.uix.image import Image


class ModePopup(Popup):
    callback = None

    def on_eco(self, obj):
        if self.callback:
            try:
                self.callback(0)
            except RuntimeError:
                pass
        self.dismiss()

    def on_standard(self, obj):
        if self.callback:
            try:
                self.callback(1)
            except RuntimeError:
                pass
        self.dismiss()

    def on_track(self, obj):
        if self.callback:
            try:
                self.callback(2)
            except RuntimeError:
                pass
        self.dismiss()

    def __init__(self, **kwargs):
        self.title = 'Select mode'

        box_layout = BoxLayout(orientation='horizontal')

        b_eco = ImageButton(source='images/Mode_ECO.png')
        b_eco.bind(on_press=self.on_eco)
        b_standard = ImageButton(source='images/Mode_Standard.png')
        b_standard.bind(on_press=self.on_standard)
        b_track = ImageButton(source='images/Mode_Track.png')
        b_track.bind(on_press=self.on_track)

        box_layout.add_widget(b_eco)
        box_layout.add_widget(b_standard)
        box_layout.add_widget(b_track)

        self.content = box_layout
        self.title = 'Select Mode'

        super(ModePopup, self).__init__(**kwargs)

    def set_callback(self, callback):
        self.callback = callback


class ModeView(AnchorLayout):
    mode_button = None

    emilio_counter = 0

    def on_mode_changed(self, mode):
        pass

    def callback(self, mode):
        if mode == 0:
            self.mode_button.source = 'images/Mode_ECO.png'
            self.emilio_counter += 1
            if self.emilio_counter == 3:
                popup = Popup(title='seriously?', content=Image(source='images/emilio.png'), size_hint=(0.3, 0.5))
                popup.open()
        if mode == 1:
            self.mode_button.source = 'images/Mode_Standard.png'
            self.emilio_counter = 0
        if mode == 2:
            self.mode_button.source = 'images/Mode_Track.png'
            self.emilio_counter = 0

    def __init__(self, **kwargs):
        super(ModeView, self).__init__(**kwargs)

        self.mode_button = ImageButton(source='images/Mode_Standard.png')

        self.mode_button.bind(on_press=self.on_select)

        self.add_widget(self.mode_button)

    def on_select(self, a):
        window = ModePopup(size_hint=(0.6, 0.5))
        window.set_callback(self.callback)
        window.open()
