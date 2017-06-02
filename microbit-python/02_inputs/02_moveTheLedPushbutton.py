import microbit as mb


def main():
    x_value = 0
    y_value = 0
    while True:
        # if mb.button_a.was_pressed():
        if mb.pin0.read_digital():
            x_value = x_value + 1
            if x_value > 4:
                x_value = 0
        # if mb.button_b.was_pressed():
        if mb.pin8.read_digital():
            y_value = y_value + 1
            if y_value > 4:
                y_value = 0
        mb.display.clear()
        mb.display.set_pixel(x_value, y_value, 9)
        mb.sleep(200)


main()
