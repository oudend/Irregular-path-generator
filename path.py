import matplotlib.pyplot as plt

import numpy, random, extra


class Path:
  """Generate irregular path between two points"""

  def __init__(self, p1, p2):
    self.p1, self.p2 = p1, p2
  
    center = extra.midpoint(p1, p2)

    degrees = 90

    rotatedP1 = extra.rotate(center, p1, degrees)

    rotatedP2 = extra.rotate(center, p2, degrees)

    self.direction = extra.direction(rotatedP1[0], rotatedP1[1], rotatedP2[0], rotatedP2[1])


  def generate(self, segments, strength, changePoint=5):

    points = list(zip(numpy.linspace(self.p1[0], self.p2[0], segments+1), numpy.linspace(self.p1[1], self.p2[1], segments+1)))

    centerStrength = 0
    offset = 0


    self.result = []

    for x in range(len(points)):

      if x < changePoint:
        centerStrength += 1/changePoint 
      elif x > len(points) - changePoint - 1:
        centerStrength -= 1/changePoint

      offset += random.uniform(-strength, strength)

      offset *= centerStrength

      offset = min(max(-strength, offset), strength, offset)

      self.result.append((
        points[x][0] + self.direction[0]*offset,
        points[x][1] + self.direction[1]*offset
      ))

    return self.result

      

  def visualize(self, pSize=10):

    x, y = zip(*self.result)

    startX, startY = zip(*[self.p1,self.p2])

    plt.scatter(x, y, pSize)

    plt.scatter(startX, startY, pSize+2, 'red')

    plt.show()  
