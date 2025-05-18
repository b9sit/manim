from manim import *
from manim import rate_functions as rf
import numpy as np

class MercRev(MovingCameraScene):
    def construct(self):
        rad = 2
        base_angle = np.pi / 2
        rotation_tracker = ValueTracker(0)

        angles = [base_angle, base_angle + 2 * np.pi / 3, base_angle + 4 * np.pi / 3]
        points = [np.array([rad * np.cos(a), rad * np.sin(a), 0]) for a in angles]

        base = Circle(radius=rad, color=WHITE)
        lines = VGroup(*[Line(ORIGIN, points[i], color=WHITE) for i in range(3)])
        mercLogo = VGroup(base, lines)

        mercLogo.scale(0.3)
        mercLogo.move_to([0, 2, 0])

        top_left = [-1, 0, 0]
        top_right = [1, 0, 0]
        bottom_right = [2, -1, 0]
        bottom_left = [-2, -1, 0]

        trapezium = Polygon(top_left, top_right, bottom_right, bottom_left, color=WHITE)
        rectangle = Rectangle(width=6, height=1, color=WHITE)
        rectangle.next_to(trapezium, DOWN, buff=0)
        rectangle.shift(RIGHT * 0.5)

        tire1 = Circle(radius=0.4)
        tire1.set_fill(BLACK, opacity=1)        
        tire1.set_stroke(WHITE, width=3)         
        tire1.next_to(trapezium, DOWN, buff=0.6)
        tire1.shift(LEFT * 1.5)

        tire2 = Circle(radius=0.4, color=WHITE)
        tire2.set_fill(BLACK, opacity=1)
        tire2.set_stroke(WHITE, width=3)         
        tire2.next_to(trapezium, DOWN, buff=0.6)
        tire2.shift(RIGHT * 2)

        tire1.set_z_index(2)
        tire2.set_z_index(2)
        
        tires = VGroup(tire1, tire2)
        
        car = VGroup(trapezium, rectangle, tires)
        car.move_to([-12, -2, 0])

        text = Text("Mercedes")
        text.next_to(mercLogo, DOWN, buff=0.2)

        logo = VGroup(mercLogo, text)
    
        self.play(
        AnimationGroup(
        Rotate(mercLogo, angle=TAU*3, run_time=2, rate_func=rf.ease_out_sine),
        car.animate.move_to([0, -2, 0]),
        lag_ratio=0.5,
        run_time=2,
        rate_func=rf.ease_out_sine
            )
        )
        self.play(FadeIn(text, rate_func=rf.ease_out_sine))
        self.play(
        self.camera.frame.animate.move_to(logo).scale(0.5), run_time=0.5, rate_func=rf.ease_out_sine)

        self.wait(1)
