import ev3dev.ev3 as ev3


def main():
    print("--------------------------------------------")
    print("  Hello Dave")
    print("--------------------------------------------")
    ev3.Sound.speak("Hello Dave").wait()


main()
