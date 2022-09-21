input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("YES")
    music.playTone(131, music.beat(BeatFraction.Whole))
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    radio.sendString("NO")
    music.playTone(262, music.beat(BeatFraction.Whole))
})
radio.setGroup(1)
radio.sendString("R U OK?")
music.playTone(262, music.beat(BeatFraction.Whole))
music.playTone(131, music.beat(BeatFraction.Whole))
music.playTone(262, music.beat(BeatFraction.Whole))
basic.forever(function on_forever() {
    
})
