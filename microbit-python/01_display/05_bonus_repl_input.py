import microbit as mb

def main():
    name = input("What is your name? ")
    mb.display.scroll("Hello " + name)


main()
