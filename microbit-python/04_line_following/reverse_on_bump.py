import microbit as mb

# Outputs:
#  pin16 (left forward)
#  pin12 (right forward)
#  pin0 (left reverse)
#  pin8 (right reverse)

# Inputs:
#  pin2 (left line sensor)
#  pin1 (right line sensor)


def main():
    mb.display.show(mb.Image.GIRAFFE)
    while True:
        if mb.button_a.is_pressed():
            drive_until_bump()
            back_up()


def drive_until_bump():
    speed = 400
    acc_threshold = 200
    mb.pin12.write_analog(speed)
    mb.pin16.write_analog(speed)
    mb.display.show("F")
    mb.sleep(2000)
    while True:
        if mb.accelerometer.get_z() > acc_threshold:
            break
    mb.pin12.write_analog(0)
    mb.pin16.write_analog(0)


def back_up():
    mb.pin0.write_analog(400)
    mb.pin8.write_analog(400)
    mb.display.show("R")
    mb.sleep(1000)
    mb.pin0.write_analog(0)
    mb.display.show("T")
    mb.sleep(1000)
    mb.pin8.write_analog(0)
    mb.display.show("S")


main()
