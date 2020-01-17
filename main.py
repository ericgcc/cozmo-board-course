import time
import cozmo
from cozmo.objects import CustomObject
from cozmo.util import degrees, distance_mm, speed_mmps
from custom_map import CustomMap

def cozmo_program(robot: cozmo.robot.Robot):
    # réinitialisation des objets
    robot.world.delete_all_custom_objects()
    print(robot.pose.position)

    m = CustomMap(robot)

    action = robot.go_to_pose(m.stop_1, relative_to_robot=False)
    action.wait_for_completed()

    action = robot.go_to_pose(m.stop_2, relative_to_robot=False)
    action.wait_for_completed()

    action = robot.go_to_pose(m.stop_3, relative_to_robot=False)
    action.wait_for_completed()

    action = robot.go_to_pose(m.stop_4, relative_to_robot=False)
    action.wait_for_completed()

    action = robot.go_to_pose(m.stop_5, relative_to_robot=False)
    action.wait_for_completed()

    action = robot.go_to_pose(m.stop_6, relative_to_robot=False)
    action.wait_for_completed()

    while True:
        time.sleep(1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)