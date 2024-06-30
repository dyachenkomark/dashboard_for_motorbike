import can
from sources.can.controller import Controller
import sources.platform as platform


class CanListener(can.Listener):
    def __init__(self, dashboard):
        self.dashboard = dashboard
        pass

    def on_message_received(self, msg):
        if msg.arbitration_id == Controller.MSG_RPM:
            rpm = platform.bytes_to_int16(msg.data[0], msg.data[1])
            self.dashboard.speed = platform.rpm_to_speed(rpm)
            pass

