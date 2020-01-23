import time
from time import strftime
import datetime
import sys
import os

import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

# GLOBALS
directory = '.'
liveCamera = False
global_robot = None

def on_new_camera_image(evt, **kwargs):
    global liveCamera
    if liveCamera:
        print("Cozmo is taking a photo")
        pilImage = kwargs['image'].raw_image
        global directory
        pilImage.save(f"photos/{directory}_2/{directory}-{kwargs['image'].image_number}.jpeg", "JPEG")

def photo():
    global liveCamera

    # Make sure Cozmo's head and arm are at a reasonable level
    # robot.set_head_angle(degrees(0.0)).wait_for_completed()
    global_robot.set_lift_height(0.0).wait_for_completed()

    liveCamera = True
    time.sleep(0.1)
    liveCamera = False

def setup_camera(robot: cozmo.robot.Robot):
    global global_robot
    global_robot = robot

    # Whenever Cozmo sees a "new" image, take a picture
    robot.add_event_handler(cozmo.world.EvtNewCameraImage, on_new_camera_image)

    # Indicate the directory to store the photos
    global directory
    directory = f"{strftime('%y%m%d')}"
    if not os.path.exists('photos'):
        os.makedirs('photos')
    if not os.path.exists(f'photos/{directory}_2'):
        os.makedirs(f'photos/{directory}_2')