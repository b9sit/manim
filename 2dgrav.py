from manim import *
from manim import rate_functions as rf
import numpy as np

class TwoDimGrav(MovingCameraScene):
    def construct(self):
        warpStrength = ValueTracker(0)

        points = 60
        xVals = np.linspace(-self.camera.frame_width / 2, self.camera.frame_width / 2, points)
        vertices = [np.array([x, 0, 0]) for x in xVals]
        colors = color_gradient([RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE], points)
        dots = VGroup(*[Dot(point=v, color=c, radius=0.07) for v, c in zip(vertices, colors)])
        self.add(dots)

        planet = Circle(radius=0.5, color=DARK_BLUE, fill_opacity=1)
        planet.move_to([0,3,0])
        self.add(planet)

        distance = ValueTracker(planet.get_bottom()[1])

        def updateDistance(m):
            distance.set_value(m.get_bottom()[1])
            print(distance.get_value())

        planet.add_updater(updateDistance)

        def checkProx(m):
           if distance.get_value() < 0.01:
                warpStrength.increment_value(0.05)

        self.add_updater(checkProx)
               
        def calculateDx(m):
            dx = m.get_center()[0] - planet.get_center()[0]
            dip = -warpStrength.get_value() * np.exp(-dx**2)
            m.move_to([m.get_center()[0], dip, 0])

        for dot in dots:
            dot.add_updater(calculateDx)

        self.wait(1)

        self.play(planet.animate.move_to([0, -2, 0]))