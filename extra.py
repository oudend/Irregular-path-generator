import math

def distance(p1, p2):
  dist = math.sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
  return dist

def midpoint(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

def rotate(origin, point, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)
    return qx, qy

def normalize(x, y):

  length = math.sqrt(x ** 2 + y ** 2);

  x /= length
  y /= length

  return (x, y)

def direction(x1, y1, x2, y2):
  return normalize(x2 - x1, y2 - y1)
