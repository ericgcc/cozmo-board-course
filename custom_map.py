import cozmo
from cozmo.util import degrees, Pose

class CustomMap:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot
        self.stop_1 = Pose(695.86, 0, 0, angle_z=degrees(0))
        self.stop_2 = Pose(745, -700, 0, angle_z=degrees(0))
        self.stop_3 = Pose(225, -420, 0, angle_z=degrees(-90))
        self.stop_4 = Pose(150, 150, 0, angle_z=degrees(0))
        self.stop_5 = Pose(350, 550, 0, angle_z=degrees(-90))
        self.stop_6 = Pose(50, 350, 0, angle_z=degrees(180))
        self.stop_7 = Pose(0, 0, 0, angle_z=degrees(180))

        self.WALL_HEIGHT = 25.04  # mm
        self.WALL_WIDTH = 11.73  # mm

        self.create_walls()

    def create_walls(self):
        # --- VERTICAL WALLS ---
        vw1_center = Pose(60.96, 123.23, 0,  angle_z=degrees(0))
        vw1 = self.robot.world.create_custom_fixed_object(vw1_center, 98.45, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw2_center = Pose(49.73, -124.66, 0,  angle_z=degrees(0))
        vw2 = self.robot.world.create_custom_fixed_object(vw2_center, 98.45, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw3_center = Pose(458.9, 446.38, 0,  angle_z=degrees(0))
        vw3 = self.robot.world.create_custom_fixed_object(vw3_center, 917.80, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw4_center = Pose(458.9, -398.24, 0,  angle_z=degrees(0))
        vw4 = self.robot.world.create_custom_fixed_object(vw4_center, 917.80, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw5_center = Pose(362.41, 120.9, 0,  angle_z=degrees(0))
        vw5 = self.robot.world.create_custom_fixed_object(vw5_center, 201.36, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw6_center = Pose(236.2, -125, 0,  angle_z=degrees(0))
        vw6 = self.robot.world.create_custom_fixed_object(vw6_center, 51.08, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw7_center = Pose(473.17, -97.04, 0,  angle_z=degrees(0))
        vw7 = self.robot.world.create_custom_fixed_object(vw7_center, 73.69, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        vw8_center = Pose(837.29, 5.87, 0,  angle_z=degrees(0))
        vw8 = self.robot.world.create_custom_fixed_object(vw8_center, 137.54, self.WALL_WIDTH, self.WALL_HEIGHT, relative_to_robot=False)

        # --- HORIZONTAL WALLS ---
        hw1_center = Pose(5.87, 225.54, 0,  angle_z=degrees(0))
        hw1 = self.robot.world.create_custom_fixed_object(hw1_center, self.WALL_WIDTH, 370.97, self.WALL_HEIGHT, relative_to_robot=True)

        hw2_center = Pose(5.87, -237.66, 0,  angle_z=degrees(0))
        hw2 = self.robot.world.create_custom_fixed_object(hw2_center, self.WALL_WIDTH, 309.44, self.WALL_HEIGHT, relative_to_robot=True)

        hw3_center = Pose(912.44, 23.7, 0,  angle_z=degrees(0))
        hw3 = self.robot.world.create_custom_fixed_object(hw3_center, self.WALL_WIDTH, 833.4, self.WALL_HEIGHT, relative_to_robot=True)

        hw4_center = Pose(255.87, 264, 0,  angle_z=degrees(0))
        hw4 = self.robot.world.create_custom_fixed_object(hw4_center, self.WALL_WIDTH, 351.98, self.WALL_HEIGHT, relative_to_robot=True)

        hw5_center = Pose(255.87, -105.57, 0,  angle_z=degrees(0))
        hw5 = self.robot.world.create_custom_fixed_object(hw5_center, self.WALL_WIDTH, 27.02, self.WALL_HEIGHT, relative_to_robot=True)

        hw6_center = Pose(442.19, -247.5, 0,  angle_z=degrees(0))
        hw6 = self.robot.world.create_custom_fixed_object(hw6_center, self.WALL_WIDTH, 289.75, self.WALL_HEIGHT, relative_to_robot=True)

        hw7_center = Pose(504.14, -71.51, 0,  angle_z=degrees(0))
        hw7 = self.robot.world.create_custom_fixed_object(hw7_center, self.WALL_WIDTH, 39.93, self.WALL_HEIGHT, relative_to_robot=True)

        hw8_center = Pose(605.87, 302.74, 0,  angle_z=degrees(0))
        hw8 = self.robot.world.create_custom_fixed_object(hw8_center, self.WALL_WIDTH, 274.52, self.WALL_HEIGHT, relative_to_robot=True)

        hw9_center = Pose(618.13, 158.79, 0,  angle_z=degrees(45))
        hw9 = self.robot.world.create_custom_fixed_object(hw9_center, self.WALL_WIDTH, 45.85, self.WALL_HEIGHT, relative_to_robot=True)

        hw10_center = Pose(761.56, 17.52, 0,  angle_z=degrees(45))
        hw10 = self.robot.world.create_custom_fixed_object(hw10_center, self.WALL_WIDTH, 45.85, self.WALL_HEIGHT, relative_to_robot=True)

        # if None not in (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14):
        #    print("fixed_objects created successfully")
        #    return (wall1, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11, wall12, wall13, wall14)

        # print("An error occurred creating walls")
        # return None