import time
import cozmo
from cozmo.objects import CustomObject
from cozmo.util import degrees, distance_mm, speed_mmps
from custom_map import CustomMap

ROBOT: cozmo.robot.Robot = None

def cozmo_program(robot: cozmo.robot.Robot):
    global ROBOT
    ROBOT = robot

    # réinitialisation des objets
    robot.world.delete_all_custom_objects()
    print(robot.pose.position)

    m = CustomMap(robot)

    action_04(robot)

    # action = robot.go_to_pose(m.stop_1, relative_to_robot=False)
    # action.wait_for_completed()

    # action = robot.go_to_pose(m.stop_2, relative_to_robot=False)
    # action.wait_for_completed()

    # action = robot.go_to_pose(m.stop_3, relative_to_robot=False)
    # action.wait_for_completed()

    # action = robot.go_to_pose(m.stop_4, relative_to_robot=False)
    # action.wait_for_completed()

    # action = robot.go_to_pose(m.stop_5, relative_to_robot=False)
    # action.wait_for_completed()

    # action = robot.go_to_pose(m.stop_6, relative_to_robot=False)
    # action.wait_for_completed()

    while True:
        time.sleep(1)

def action_04(robot):
    print("*** action 04: Play a song ***")

    # Create an array of SongNote objects, consisting of all notes from C2 to C3_Sharp
    notes = [
        cozmo.song.SongNote(cozmo.song.NoteTypes.E2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.A2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.C2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.B2, cozmo.song.NoteDurations.Quarter),
        cozmo.song.SongNote(cozmo.song.NoteTypes.D2, cozmo.song.NoteDurations.Quarter),
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
    robot.play_song(notes, loop_count=1).wait_for_completed()

cozmo.run_program(cozmo_program, use_3d_viewer=True, use_viewer=True)