import microbit as mb
import music


def main():
    loops = 1
    mb.display.show(mb.Image.MUSIC_QUAVER)
    while True:
        if mb.button_a.is_pressed():
            loops = loops + 1
            mb.display.show(str(loops))
            playNoteLights(loops, 80)
        if mb.button_b.is_pressed():
            goCrazy(loops)


def lightLed(ledNumber):
    if ledNumber == 0:
        # All off
        mb.pin1.write_digital(0)
        mb.pin2.write_digital(0)
        mb.pin16.write_digital(0)
    elif ledNumber == 1:
        mb.pin1.write_digital(1)
        mb.pin2.write_digital(0)
        mb.pin16.write_digital(0)
    elif ledNumber == 2:
        mb.pin1.write_digital(0)
        mb.pin2.write_digital(1)
        mb.pin16.write_digital(0)
    elif ledNumber == 3:
        mb.pin1.write_digital(0)
        mb.pin2.write_digital(0)
        mb.pin16.write_digital(1)


def playNoteLights(n, tempo):
    '''Plays n loops of three notes'''
    music.set_tempo(bpm=tempo)
    for i in range(n):
        lightLed(1)
        music.play('c4:1')
        lightLed(2)
        music.play('d4:1')
        lightLed(3)
        music.play('e4:2')
    lightLed(0)


def goCrazy(n):
    delayMs = 150
    music.play(music.RINGTONE, wait=False)
    for i in range(n):
        lightLed(1)
        mb.sleep(delayMs)
        lightLed(2)
        mb.sleep(delayMs)
        lightLed(3)
        mb.sleep(delayMs)
        lightLed(2)
        mb.sleep(delayMs)
    lightLed(0)


main()
