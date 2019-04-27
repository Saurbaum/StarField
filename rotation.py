"""Rotation library"""

import math

def rotate_point(offset, angle, point):
    """Rotate a point around an origin"""
    sin = math.sin(math.radians(angle))
    cos = math.cos(math.radians(angle))

    # Translate point back to origin:
    x_origin = point[0] - offset[0]
    y_origin = point[1] - offset[1]

    # Rotate point
    x_new = x_origin * cos - y_origin * sin
    y_new = x_origin * sin + y_origin * cos

    # Translate point back:
    return (x_new + offset[0], y_new + offset[1])

def get_angle(x_offset, y_offset):
    """Get the angle between 2 points"""
    angle = math.degrees(math.atan2(y_offset, x_offset))

    if angle < 0:
        angle += 360

    return angle
