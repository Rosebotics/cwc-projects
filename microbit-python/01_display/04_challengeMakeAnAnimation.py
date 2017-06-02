import microbit as mb


def main():
    boat1 = mb.Image("05050:"
                     "05050:"
                     "05050:"
                     "99999:"
                     "09990")

    boat2 = mb.Image("00000:"
                     "05050:"
                     "05050:"
                     "05050:"
                     "99999")

    boat3 = mb.Image("00000:"
                     "00000:"
                     "05050:"
                     "05050:"
                     "05050")

    boat4 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "05050:"
                     "05050")

    boat5 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "05050")

    boat6 = mb.Image("00000:"
                     "00000:"
                     "00000:"
                     "00000:"
                     "00000")

    all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    mb.display.show(all_boats, delay=300, loop=True)


main()
