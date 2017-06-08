#!/usr/bin/env python3
import ev3dev.ev3 as ev3
import time


def main():
    print("--------------------------------------------")
    print(" Buttons with LEDs")
    print("--------------------------------------------")
    ev3.Sound.speak("Buttons with L E Dees").wait()

    # Opening LED dance (to show the LED syntax)
    # Red LEDs
    ev3.Sound.speak("Red")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.RED)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
    time.sleep(3)

    # Green LEDs
    ev3.Sound.speak("Green")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    time.sleep(3)

    # Turn LEDs off
    ev3.Sound.speak("Off")
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)

    # Buttons on EV3 (the real focus of this module)
    btn = ev3.Button()  # Construct the one and only EV3 Button object

    while True:
        if btn.left:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.BLACK)
        if btn.right:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.BLACK)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.RED)
        if btn.up:
            ev3.Leds.all_off()  # Could also use ev3.Leds.BLACK for both LEDs
        if btn.down:
            ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.AMBER)
            ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.AMBER)
        if btn.backspace:
            break
        time.sleep(0.01)  # Best practice to avoid working too hard.

    # Best practice to leave the LEDs on after you finish a program so you don't put away the robot while still on.
    ev3.Leds.set_color(ev3.Leds.LEFT, ev3.Leds.GREEN)
    ev3.Leds.set_color(ev3.Leds.RIGHT, ev3.Leds.GREEN)
    ev3.Sound.speak("Goodbye").wait()


main()
