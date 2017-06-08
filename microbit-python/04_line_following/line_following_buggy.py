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
    white_value = 0
    fast_speed = 400
    slow_speed = 0  # Faster is better

    mb.pin0.write_digital(0)
    mb.pin8.write_digital(0)

    while True:
        # Left side
        if mb.pin2.read_digital() == white_value:
            mb.pin16.write_analog(fast_speed)
            # mb.display.set_pixel(4, 0, 9)
        else:
            mb.pin16.write_analog(slow_speed)
            # mb.display.set_pixel(4, 0, 0)

        # Right side
        if mb.pin1.read_digital() == white_value:
            mb.pin12.write_analog(fast_speed)
            # mb.display.set_pixel(0, 0, 9)
        else:
            mb.pin12.write_analog(slow_speed)
            # mb.display.set_pixel(0, 0, 0)

        mb.sleep(50)


main()
