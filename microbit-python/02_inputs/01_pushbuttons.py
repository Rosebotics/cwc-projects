import microbit as mb
import random


def main():
    counter = 0
    mb.display.show(mb.Image.TARGET)
    # while True:
    #    if mb.button_a.is_pressed():
    #        mb.display.show(mb.Image.HAPPY)
    #    else:
    #        mb.display.show(mb.Image.ANGRY)
    while True:
        if mb.button_a.was_pressed():
            counter = counter + 1
            mb.display.scroll(str(counter))
        if mb.button_b.was_pressed():
            random_value = random.randint(1, 100)
            mb.display.scroll(str(random_value))

        # if mb.pin0.read_digital():
        #    mb.display.show(mb.Image.HAPPY)
        # else:
        #    mb.display.show(mb.Image.SAD)
            
        if mb.pin0.read_digital():
            mb.display.scroll("Hi")
        if mb.pin8.read_digital():
            mb.display.scroll("Dave")


main()
