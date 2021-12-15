from path import Path 
from extra import distance

p1 = (-100, -100)
p2 = (400, 200)

segments = int(distance(p1, p2)/10)

path = Path(p1, p2)

path.generate(segments=segments, strength=5)

path.visualize()
