from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.modules.console import ConsoleAddon

consolescreen_layout = '''
<ConsoleScreen>:
    scroll_view: scroll_view
    BoxLayout:
        orientation: 'vertical'
        Button:
            size_hint: 1.0, 0.1
            text: 'DASHBOARD'
            font_size: 30
            on_release: app.root.current = 'main'
        ScrollView:
            id: scroll_view
'''

Builder.load_string(consolescreen_layout)


class ConsoleScreen(Screen):
    def __init__(self, **kw):
        super(ConsoleScreen, self).__init__(**kw)

