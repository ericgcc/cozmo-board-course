import cozmo
from cozmo.util import degrees, Pose
import random

class CustomMap:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot
        stop_1 = Pose(200, 250, 0, angle_z=degrees(135))
        stop_2 = Pose(200, -275, 0, angle_z=degrees(180))
        stop_3 = Pose(450, 250, 0, angle_z=degrees(45))
        stop_4 = Pose(750, 300, 0, angle_z=degrees(90))
        stop_5 = Pose(750, -150, 0, angle_z=degrees(-45))
        stop_6 = Pose(0, 0, 0, angle_z=degrees(0))
        self.stops = [stop_1, stop_2, stop_3, stop_4, stop_5]
        random.shuffle(self.stops)
        self.stops.append(stop_6)

        self.WALL_HEIGHT = 36.957  # mm
        self.WALL_WIDTH = 16.383  # mm

        self.create_walls()

    def create_walls(self):

        verticals = []
        horizontals = []

        # --- VERTICAL WALLS ---
        center = Pose(441.847, 454.078, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 850.875, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(87.12, 107.165, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 141.826, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(396.572, 103.167, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 159.525, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(79.487, -153.02, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 125.374, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(282.691, -150.278, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 37.76, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(780.018, -25, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 175.313, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        center = Pose(442.247, -412.401, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, 850.875, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)
        verticals.append(wall)

        # --- HORIZONTAL WALLS ---
        center = Pose(8.616, 281.021, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 363.322, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(8.616, -282.713, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 275.793, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(308.57, 245.504, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 400.738, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(308.57, -126.38, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 47.777, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(508.616, -299.173, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 210.055, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(525.781, -184.775, self.WALL_HEIGHT/2,  angle_z=degrees(315))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 64.186, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(608.616, 260.69, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 370.367, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(682.84, -43.71, self.WALL_HEIGHT/2,  angle_z=degrees(315))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 66.213, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        center = Pose(875.879, 20.836, self.WALL_HEIGHT/2,  angle_z=degrees(0))
        wall = self.robot.world.create_custom_fixed_object(center, self.WALL_WIDTH, 882.891, self.WALL_HEIGHT, relative_to_robot=True)
        horizontals.append(wall)

        if None not in verticals and None not in horizontals:
            print("fixed_objects created successfully")
            return verticals, horizontals

        print("An error occurred creating walls")
        return None