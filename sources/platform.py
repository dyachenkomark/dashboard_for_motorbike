import math

SPROCKET_FRONT = 13
SPROCKET_REAR = 50
SPROCKET_RATIO = SPROCKET_FRONT / SPROCKET_REAR
TIRE_RADIUS = 0.3


def rpm_to_speed(rpm):
    speed = 12 / 100 * math.pi * TIRE_RADIUS * SPROCKET_RATIO * rpm
    return speed


def bytes_to_int16(b1, b2):
    return b1 << 8 | b2

