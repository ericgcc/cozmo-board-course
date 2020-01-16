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


    while True:
        time.sleep(1)

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)