import time

import cozmo
from cozmo.objects import CustomObject
from custom_objects import objects, custom_object_pose
from custom_map import CustomMap
from action_manager import ActionManager
from take_photo import setup_camera, photo

objs = None
stops = 0
am = None
stops_visited = []

def handle_object_appeared(evt, **kw):
    # This will be called each time an EvtObjectAppeared is triggered
    # whenever an object comes into view
    if isinstance(evt.obj, CustomObject):
        print(f"Cozmo started seeing a type: {str(evt.obj.object_type)} id: {str(evt.obj.object_id)}")

def perfom(robot: cozmo.robot.Robot):
    global stops
    found = False

    while not found:
        # Looking for the objects
        lookaround = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        objs = robot.world.wait_until_observe_num_objects(num=1, object_type=CustomObject, timeout=30)
        lookaround.stop()

        if objs[0].object_type in stops_visited:
            found = False
        else:
            stops_visited.append(objs[0].object_type)
            found = True

    if len(objs) > 0:
        stops += 1
        photo()
        robot.say_text(f"Arrête {stops}").wait_for_completed()
        am.launch(objs[0])
    else:
        print("Cannot locate custom box")

def cozmo_program(robot: cozmo.robot.Robot):
    global objs
    global am

    # Event handlers every time Cozmo sees or stops seeing an object
    robot.add_event_handler(cozmo.objects.EvtObjectAppeared, handle_object_appeared)

    # Objects reinit
    robot.world.delete_all_custom_objects()
    print(robot.pose.position)

    m = CustomMap(robot)
    objs = objects(robot)
    am = ActionManager(robot)
    setup_camera(robot)

    # Stop 1
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    perfom(robot)
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)

    # Stop 2
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    perfom(robot)
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)

    # Stop 3
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    perfom(robot)
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)

    # Stop 4
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    perfom(robot)
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)

    # Stop 5
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    perfom(robot)
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)

    # Stop 6
    action = robot.go_to_pose(m.stops.pop(0), relative_to_robot=False)
    action.wait_for_completed()
    print("Completed action: result = %s" % action)
    print("New robot position =", robot.pose.position)
    robot.play_anim_trigger(cozmo.anim.Triggers.SparkSuccess).wait_for_completed()

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)