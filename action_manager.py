import time
from PIL import Image

import cozmo
from cozmo.util import degrees
from cozmo.objects import CustomObjectTypes

class ActionManager:

    def __init__(self, robot: cozmo.robot.Robot):
        self.robot = robot

    def launch(self, custom_object):
        switcher={
            CustomObjectTypes.CustomType00: self.action_00,
            CustomObjectTypes.CustomType01: self.action_01,
            CustomObjectTypes.CustomType02: self.action_02,
            CustomObjectTypes.CustomType03: self.action_03,
            CustomObjectTypes.CustomType04: self.action_04,
        }
        func=switcher.get(custom_object.object_type, lambda :"Invalid type")
        return func()


    def action_00(self):
        print("** action 00: OLED face ***")

        # Ouvre le fichier d'image
        img = Image.open('ETS-blanc.png')

        # Change la résolution originale de l'image dans une que l'écran peut afficher avec l'algo BICUBIC
        resized = img.resize(cozmo.oled_face.dimensions(), Image.BICUBIC)

        # Transforme l'image dans un format que l'écran peut afficher
        face = cozmo.oled_face.convert_image_to_screen_data(resized)

        self.robot.set_head_angle(cozmo.robot.MAX_HEAD_ANGLE).wait_for_completed()
        # Afficher l'image pendant 2000 ms
        self.robot.display_oled_face_image(face, 2000).wait_for_completed()
        self.robot.set_head_angle(degrees(0)).wait_for_completed()

    def action_01(self):
        print("*** action 01: Playing animation ***")
        self.robot.play_anim_trigger(cozmo.anim.Triggers.DanceMambo).wait_for_completed()

    def action_02(self):
        print("*** action 02: Cubes Stack ***")
        print("!!! .: SHOW COZMO TWO CUBES :. !!!")

        # Essai d'émpiler 2 cubes
        # Regarde autour de soi, jusqu'à ce que Cozmo sache où sont au moins 2 cubes :
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cubes = self.robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cubes) < 2:
            print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
        else:
            # Essai de ramasser le 1er cube
            current_action = self.robot.pickup_object(cubes[0], num_retries=3)
            current_action.wait_for_completed()
            if current_action.has_failed:
                code, reason = current_action.failure_reason
                result = current_action.result
                print("Pickup Cube failed: code=%s reason='%s' result=%s" % (code, reason, result))
                return

            # Maintenant, essai de placer ce cube sur le 2ème.
            current_action = self.robot.place_on_object(cubes[1], num_retries=3)
            current_action.wait_for_completed()


    def action_03(self):
        print("*** action 03: Cubes unstack ***")
        print("!!! .: SHOW COZMO TWO STACKED CUBES :. !!!")
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cubes = self.robot.world.wait_until_observe_num_objects(num=2, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cubes) < 2:
            print("Error: need 2 Cubes but only found", len(cubes), "Cube(s)")
        else:
            pickup = self.robot.pickup_object(cubes[1], num_retries=3).wait_for_completed()
            self.robot.turn_in_place(degrees(90)).wait_for_completed()
            self.robot.place_object_on_ground_here(cubes[1]).wait_for_completed()

            if not pickup:
                self.robot.pickup_object(cubes[0], num_retries=3).wait_for_completed()
                self.robot.turn_in_place(degrees(90)).wait_for_completed()
                self.robot.place_object_on_ground_here(cubes[0]).wait_for_completed()

    def action_04(self):
        print("*** action 04: Face recognition ***")
        findfaces= self.robot.start_behavior(cozmo.behavior.BehaviorTypes.FindFaces)
        face = self.robot.world.wait_for_observed_face(timeout=None, include_existing=True)
        findfaces.stop()

        if face is not None:
            self.robot.say_text(f"{face.name}").wait_for_completed()