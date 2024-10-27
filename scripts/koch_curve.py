from manim import *



class KochCurve(Scene):
    def construct(self):
        def KochCurve(n, length=12, stroke_width=8, color=BLUE):
            l = length / (3 ** n)
            line_group = Line().set_length(l)

            def next_level(line_group):
                return VGroup(
                    *[line_group.copy().rotate(i) for i in [0, PI / 3, -PI / 3, 0]]
                ).arrange(RIGHT, buff=0, aligned_edge=DOWN)
            
            for _ in range(n):
                line_group = next_level(line_group)

            KC = (
                VMobject(stroke_width=stroke_width)
                .set_points(line_group.get_all_points())
                .set_color(color)
            )
            return KC

        level = Variable(0, "level", var_type=Integer).set_color(WHITE)
        txt = (
            VGroup(Tex("Koch Curve", font_size=60), level)
            .arrange(DOWN, aligned_edge=LEFT)
            .to_corner(UL)
        )

        init_width = 12
        nb_iterations = 8

        kc = KochCurve(0, stroke_width=init_width).to_edge(DOWN, buff=2.5)
        self.add(txt, kc)
        self.wait()
        for i in range(1, nb_iterations):
            self.play(
                level.tracker.animate.set_value(i),
                kc.animate.become(
                    KochCurve(i, stroke_width=init_width - (init_width / nb_iterations * i)
                              ).to_edge(DOWN, buff=2.5)
                ),
            )
            self.wait()
        self.wait(3)


