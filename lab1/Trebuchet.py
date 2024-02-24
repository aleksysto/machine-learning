import math
import random as random
import matplotlib.pyplot as plt
import numpy as np
# h=100m 
# starting velocity v0=50m/s
# given: angle as alpha
# target: random distance from 50m to 340m
# error margin: 5m

# distance: ( (v * sin(alpha)) + sqrt((v**2 * sin(alpha)**2) + (2 * g * h)) ) * ((v * cos(alpha)) / g)

h: int = 100
v: int = 50
g: float = 9.81

shots: int = 0
dist: int = random.randint(50, 340)

# te funkcje zalecilo AI, poczatkowo obie rzeczy liczylem w for loopie
def precalculate_angle(angle: float) -> float:
    alpha = math.radians(angle)
    return math.sin(alpha), math.cos(alpha)
def hits_target(dist: int, travel: float, margin=5) -> bool:
    return abs(dist - travel) <= margin


def create_plot(sin: float, cos: float, landing: float) -> None:
    time: list[int] = np.linspace(0, 100, 1000)

    coordinates: list[tuple] = []
    for t in time:
        x: float = v * cos * t
        y: float = (v * sin * t) - ((g * (t ** 2)) / 2) + h

        if not y < 0:
            coordinates.append((x, y))
    coordinates.append((landing, 0))
    x, y = zip(*coordinates)
    plt.plot(x, y, linestyle='-')
    plt.xlabel('Distance (m)')
    plt.ylabel('Height')
    plt.title('Projectile Motion')
    plt.grid(True)
    plt.show()

while True:
    print(f"Our target is {dist}m from the trebuchet")
    print("Provide the angle at which we are hurling the boulder")
    inp: float = float(input())
    sin, cos = precalculate_angle(inp) # to zalecilo AI
    travel: float = ( (v * sin) + (math.sqrt((v ** 2 * sin ** 2 ) + (2 * g * h))) ) * ((v * cos) / g)
    shots += 1
    print(dist, travel)
    if hits_target(dist, travel):
        print("We hit the target!")
        print(f"Number of shots: {shots}")
        create_plot(sin, cos, travel)
        break
    else:
        print("We missed...")
