import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Drive input")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive input").wait()
    robot = robo.Snatch3r()

    while True:
        speed_deg_per_second = int(input("Speed (0 to 900 dps): "))
        if speed_deg_per_second == 0:
            break
        inches_target = int(input("Distance (inches): "))
        if inches_target == 0:
            break

        robot.drive_inches(inches_target, speed_deg_per_second)

    robot.shutdown()


main()
