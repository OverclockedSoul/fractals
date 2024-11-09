from manim import *

def get_triangle_center(point1, point2, point3):
    # Calculate centroid (center of mass)
    center_x = (point1[0] + point2[0] + point3[0]) / 3
    center_y = (point1[1] + point2[1] + point3[1]) / 3
    return np.array([center_x, center_y, 0])

class SierpinskiChaos(Scene):
    def construct(self):
        outer_triangle = Triangle(color=WHITE).scale(3.5)
        vertices = outer_triangle.get_vertices()
        update_it = 100
        first_point = vertices[0]
        last_point = first_point
        list_points = []
        group_points = VGroup()
        for it in range(2000):
            rand_vertex = vertices[np.random.randint(0, 3)]
            new_point = (rand_vertex + last_point) / 2
            last_point = new_point
            list_points.append(last_point)
            group_points.add(Dot(last_point, 0.012))
            if it != 0 and it % update_it == 0:
                self.play(Create(group_points))
                group_points = VGroup()
                # self.play(*[GrowFromCenter(Dot(p, 0.007)) for p in list_points])
