from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.lang import Builder
from sources.widgets.flagview import FlagView
from sources.widgets.flagview import RoundedBox

flagscreen_layout = '''
<FlagsScreen>:
    BoxLayout:
        orientation: 'vertical'
        id: layout
        Button:
            size_hint: 1.0, 0.1
            font_size: 30
            text: 'DASHBOARD'
            on_release: app.root.current = 'main'
        GridLayout:
            id: grid
            cols: 9 
'''

Builder.load_string(flagscreen_layout)


class FlagsScreen(Screen):
    def __init__(self, **kw):
        super(FlagsScreen, self).__init__(**kw)

        self.groups = []

        for j in range(3):
            group = []
            self.ids.grid.add_widget(Label(text='CNT_FLAGS' + str(j), font_size=20))
            for i in range(8):
                flag = FlagView(name=str(i), text='DESCRIPTION')
                group.append(flag)
                self.ids.grid.add_widget(flag)
                # self.ids.grid.add_widget(FlagView(name=str(i), text="DESCRIPTION"))
                # self.ids.grid.add_widget(RoundedBox(corners=[20, 20, 20, 20], padding=10, line_width=5))
            self.groups.append(group)
