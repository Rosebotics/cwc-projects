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
    mb.display.show(mb.Image.HAPPY)
    while True:
        if mb.button_a.is_pressed():
            drive_square()
            stop()


def drive_square():
    fast_speed = 300
    slow_speed = 200
    for i in range(4):
        mb.pin12.write_analog(fast_speed)
        mb.pin16.write_analog(fast_speed)
        mb.display.show("F")
        mb.sleep(2000)
        mb.pin12.write_analog(0)
        mb.pin16.write_analog(slow_speed)
        mb.display.show("T")
        mb.sleep(3000)


def stop():
    mb.pin12.write_analog(0)
    mb.pin16.write_analog(0)
    mb.display.show("S")


main()
