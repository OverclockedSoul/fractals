# manim 0.18.0.post0
from manim import *

def get_midpoints(outer_vertices):
    return [
            (outer_vertices[0] + outer_vertices[1]) / 2,  # Midpoint of side 1
            (outer_vertices[1] + outer_vertices[2]) / 2,  # Midpoint of side 2
            (outer_vertices[2] + outer_vertices[0]) / 2   # Midpoint of side 3
    ]


class Sierpinski(Scene):
    def construct(self):        
        colors = [BLUE, GREEN, RED]
        run_times_fractal = 1
        

        # Create the outer triangle
        outer_triangle = Triangle(color=WHITE).scale(3.5)

        text_iteration = Text(f'iteration = ').next_to(outer_triangle, DOWN)
        it_text = Text("0").next_to(text_iteration)
        self.play(Write(text_iteration), Write(it_text))
        self.play(Create(outer_triangle))

        # memorize vertices for fractal creation
        list_vertices = [outer_triangle.get_vertices()]

        for it in range(5):

            new_it_text = Text(f"{it + 1}").next_to(text_iteration, RIGHT)
            self.play(Transform(it_text, new_it_text))
            
            new_list_vertices = []
            for outer_vertices in list_vertices:
                # Calculate the midpoints of the triangle's sides
                midpoints = get_midpoints(outer_vertices)

                # Calculate the midpoints of the outer triangle's sides for the inner triangle
                triangle_1 = Polygon(
                    outer_vertices[0], midpoints[0], midpoints[2], color=colors[it % len(colors)]
                )
                triangle_2 = Polygon(
                    midpoints[0], outer_vertices[1], midpoints[1], color=colors[it % len(colors)]
                )
                triangle_3 = Polygon(
                    midpoints[2], midpoints[1], outer_vertices[2], color=colors[it % len(colors)]
                )

                self.play(Create(triangle_1), Create(triangle_2), Create(triangle_3), 
                          run_time=1/(3**it))
                new_list_vertices += [triangle_1.get_vertices(), triangle_2.get_vertices(),
                                     triangle_3.get_vertices()]
                
            
            list_vertices = new_list_vertices
            
        # Hold the final image
        self.wait(2)
