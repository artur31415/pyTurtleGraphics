import math


def vec_from_angle(angle, mag = 1):
    return (mag * math.cos(angle), mag * math.sin(angle))

def vec_add(vec1, vec2):
    return (vec1[0] + vec2[0], vec1[1] + vec2[1])

def vec_mult(vec1, scalar):
    return (vec1[0] * scalar, vec1[1] * scalar)

def vec_sub(vec1, vec2):
    return (vec1[0] - vec2[0], vec1[1] - vec2[1])