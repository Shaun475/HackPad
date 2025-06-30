print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.encoder import EncoderHandler

encoder_handler = EncoderHandler()

keyboard = KMKKeyboard()
keyboard.modules = [encoder_handler]

keyboard.row_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.col_pins = (board.D4,board.D5,board.D6,board.D10)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.KP_SLASH, KC.KP_ASTERIK, KC.KP_MINUS,KC.KP_PLUS,
        KC.N7,KC.N8,KC.N9,KC.ENTER,
        KC.N4,KC.N5,KC.N6,KC.DOT,
        KC.N1,KC.N2,KC.N3,KC.N0
     
    ],

]

encoder_handler.pins = (
    (board.D7,board.D8,board.D9)
)

if __name__ == '__main__':
    keyboard.go()