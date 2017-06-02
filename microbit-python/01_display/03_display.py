import microbit as mb


def main():
    print("David Fisher can write Python!")
    # mb.display.scroll("Dave Fisher")
    # mb.display.show(mb.Image.HAPPY)
    # mb.display.show([mb.Image.ARROW_N, mb.Image.ARROW_E,
    #                  mb.Image.ARROW_S, mb.Image.ARROW_W])
    # print("Starting an infinite loop")
    # mb.display.show(mb.Image.ALL_CLOCKS, loop=True)
    xImage = mb.Image("20002:06060:00900:06060:20002")
    mb.display.show(xImage)

    image1 = mb.Image("77000:77000:00000:00000:00000")
    image2 = mb.Image("07700:07700:00000:00000:00000")
    image3 = mb.Image("00000:07700:07700:00000:00000")
    image4 = mb.Image("00000:77000:77000:00000:00000")
    mb.display.show([image1, image2, image3, image4], loop=True)


main()
