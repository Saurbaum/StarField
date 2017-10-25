import math

def rotatePoint(offset, angle, point):
    s = math.sin(math.radians(angle))
    c = math.cos(math.radians(angle))

    # Translate point back to origin:
    x = point[0] - offset[0]
    y = point[1] - offset[1]

    # Rotate point
    xNew = x * c - y * s
    yNew = x * s + y * c

    # Translate point back:
    return (xNew + offset[0], yNew + offset[1]);

def getAngle(x, y):
    angle = math.degrees(math.atan2(y, x))

    if angle < 0:
        angle += 360

    return angle