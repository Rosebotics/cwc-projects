import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    print("--------------------------------------------")
    print("  Drive square")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive square").wait()

    robot = robo.Snatch3r()

    for i in range(4):
        robot.drive_inches(12)
        robot.turn_degrees(90)

    robot.shutdown()


main()
