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
        print("*** action 02: Pop a wheelie ***")
        print("!!! .: SHOW COZMO ONE CUBES :. !!!")

        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = self.robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cube) < 1:
            print("Error: 1 cube needed")
        else:
            self.robot.pop_a_wheelie(cube, approach_angle=degrees(-90), num_retries=2)

    def action_03(self):
        print("*** action 03: Roll a cube ***")
        print("!!! .: SHOW COZMO ONE CUBE :. !!!")
        lookaround = self.robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)
        cube = self.robot.world.wait_until_observe_num_objects(num=1, object_type=cozmo.objects.LightCube, timeout=60)
        lookaround.stop()

        if len(cube) < 1:
            print("Error: 1 cube needed")
        else:
            self.robot.roll_cube(cube, approach_angle=degrees(-90), num_retries=2)

    def action_04(self):
        print("*** action 04: Play a song ***")

        # Create an array of SongNote objects, consisting of all notes from C2 to C3_Sharp
        notes = [
            cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2_Sharp, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2_Sharp, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.G2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
            cozmo.song.SongNote(cozmo.song.NoteTypes.Rest, cozmo.song.NoteDurations.Quarter) 
            ]

        # Play the ascending notes
       self.robot.play_song(notes, loop_count=1).wait_for_completed()
