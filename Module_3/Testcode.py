from uagame import Window
from time import sleep
window = Window('hello', 300, 200)
guess = window.input_string('Prompt Enter string >', 0, 0)

string_height = window.get_font_height()
x_coordinate = window.get_width() - window.get_string_width(guess)
y_coordinate = window.get_height() - string_height
window.draw_string(guess, x_coordinate, y_coordinate)

window.update()
sleep(2)
window.close()