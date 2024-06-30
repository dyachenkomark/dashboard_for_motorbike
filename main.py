import sys

from kivy.app import App
from sources.Dashboard import Dashboard

from sources.utils import is_raspberry_pi

# os.environ['KIVY_GL_BACKEND'] = 'gl'
# os.environ['KIVY_WINDOW'] = 'egl_rpi'


# Main application class
class SMCDashboardApp(App):
    canbus = None
    gpios = None
    canlistener = None

    def __init__(self, **kwargs):
        super(SMCDashboardApp, self).__init__(**kwargs)
        self.dashboard = Dashboard()

    def build(self):
        if is_raspberry_pi():
            print('Detected Raspberry Pi. Configuring interfaces')

            from sources.gpios import Gpios
            # from sources.can.canlistener import CanListener
            # import can

            self.gpios = Gpios(self.dashboard)
            self.gpios.update_all()
            # self.canlistener = CanListener(self.dashboard)
            # self.canbus = can.interface.Bus(channel='can0', bustype='socketcan')
            # can.Notifier(self.canbus, [self.canlistener])
        return self.dashboard


if __name__ == "__main__":
    old_excepthook = sys.excepthook

    def app_excepthook(exctype, value, traceback):
        if exctype == KeyboardInterrupt:
            print("Exception: Keyboard interrupt received")
        else:
            old_excepthook(exctype, value, traceback)
    sys.excepthook = app_excepthook

    SMCDashboardApp().run()
