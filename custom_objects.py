from math import sqrt

import cozmo
from cozmo.util import Pose
from cozmo.objects import CustomObject, CustomObjectMarkers, CustomObjectTypes, ObservableElement, ObservableObject

from sympy import Eq, symbols, solve
from numpy import ones,vstack
from numpy.linalg import lstsq

x, y = symbols("x y")

def line_equation(p1_x, p1_y, p2_x, p2_y):
    points = [(p1_x, p1_y),(p2_x, p2_y)]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, b = lstsq(A, y_coords, rcond=None)[0]
    return m, b

def nearest_intersection(x_o, y_o, points):
    dx_0 = (x_o - points[0][x])
    dy_0 = (y_o - points[0][y])
    dist_0 = sqrt(dx_0**2 + dy_0**2)

    dx_1 = (x_o - points[1][x])
    dy_1 = (y_o - points[1][y])
    dist_1 = sqrt(dx_1**2 + dy_1**2)

    if dist_0 < dist_1:
        return points[0]
    return points[1]

def custom_object_pose(robot, custom_object):

    print(">>> robot: ", robot.pose.position)
    print(">>> cube: ", custom_object.pose.position)

    m, b = line_equation(robot.pose.position.x, robot.pose.position.y,
                            custom_object.pose.position.x, custom_object.pose.position.y)
    print(">>> m, b: ", m, b)

    # line between cozmo and the object
    line = Eq(y - m*x, b)
    print(f">>> line: y = {m} x + {b}")

    # circle around the object
    circle = Eq((x - custom_object.pose.position.x)**2 + (y - custom_object.pose.position.y)**2, 10000)
    print(f">>> circle: (x - {custom_object.pose.position.x})**2 + (y - {custom_object.pose.position.y})**2")

    # Intersection points between line and circle
    result = solve([line, circle])
    print(">>> intesection points: ", result)

    point = nearest_intersection(robot.pose.position.x, robot.pose.position.y, result)
    print(">>> nearest intersection: ", point)

    return Pose(point[x], point[y], 0, angle_z=custom_object.pose.rotation.angle_z)

def objects(robot: cozmo.robot.Robot):

    return [robot.world.define_custom_cube(CustomObjectTypes.CustomType00,
                                                 CustomObjectMarkers.Circles4,
                                                 50, 24.19, 24.19, True),

            robot.world.define_custom_cube(CustomObjectTypes.CustomType01,
                                           CustomObjectMarkers.Hexagons4,
                                            50, 24.19, 24.19, True),

            robot.world.define_custom_cube(CustomObjectTypes.CustomType02,
                                           CustomObjectMarkers.Triangles3,
                                            50, 24.19, 24.19, True),

            robot.world.define_custom_cube(CustomObjectTypes.CustomType03,
                                           CustomObjectMarkers.Hexagons5,
                                            50, 24.19, 24.19, True),

            robot.world.define_custom_cube(CustomObjectTypes.CustomType04,
                                           CustomObjectMarkers.Diamonds3,
                                            50, 24.19, 24.19, True),
            ]