def on_button_pressed_a():
    radio.send_string("YES")
    music.play_tone(131, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)

def on_button_pressed_b():
    radio.send_string("NO")
    music.play_tone(262, music.beat(BeatFraction.WHOLE))
input.on_button_pressed(Button.B, on_button_pressed_b)

radio.set_group(1)
radio.send_string("R U OK?")
music.play_tone(262, music.beat(BeatFraction.WHOLE))
music.play_tone(131, music.beat(BeatFraction.WHOLE))
music.play_tone(262, music.beat(BeatFraction.WHOLE))

def on_forever():
    pass
basic.forever(on_forever)
