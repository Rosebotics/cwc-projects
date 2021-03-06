#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import robot_controller as robo


def main():
    print("--------------------------------------------")
    print(" Drive polygon")
    print("--------------------------------------------")
    ev3.Sound.speak("Drive polygon").wait()

    robot = robo.Snatch3r()

    while True:
        speed_deg_per_second = int(input("Speed (0 to 900 dps): "))
        if speed_deg_per_second == 0:
            break

        sides = int(input("Number of sides: "))
        # Try a negative value for Number of sides to drive CW around the polygon.
        if sides == 0:
            break
        turn_amount = 360 / sides

        edge_length_in = int(input("Length of each edge (inches): "))
        if edge_length_in == 0:
            break

        for i in range(sides):
            robot.drive_inches(edge_length_in, speed_deg_per_second)
            robot.turn_degrees(turn_amount, speed_deg_per_second)

    robot.shutdown()


main()



