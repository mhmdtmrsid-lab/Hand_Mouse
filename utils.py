import math

def distance(p1, p2):
    return math.hypot(p2.x - p1.x, p2.y - p1.y)

def map_range(val, a, b, c, d):
    return c + (val - a) * (d - c) / (b - a)
