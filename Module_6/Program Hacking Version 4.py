from uagame import Window
from time import sleep

# create window
window = Window('Hacking', 600, 500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

# GAME START
string_height = window.get_font_height()
line_y = 0

header = ['DEBUG MODE', '1 ATTEMPT(S) LEFT', '']

for header_line in header:
    window.draw_string(header_line, 0, line_y)
    window.update()
    sleep(0.5)
    line_y = line_y + string_height

# PASSWORD LIST
password_list = ['PROVIDE', 'SETTING', 'CANTINA', 'CUTTING', 'HUNTERS',
                 'SURVIVE','HEARING', 'HUNTING', 'REALIZE', 'NOTHING',
                 'OVERLAP','FINDING','PUTTING', '']

for password in password_list:
    window.draw_string(password, 0, line_y)
    window.update()
    sleep(0.5)
    line_y = line_y + string_height

# PROMPT FOR GUESS
guess = window.input_string("ENTER PASSWORD >", 0, line_y)

# CHECK THE GUESS
window.clear()
window.update()

correct_password = 'PUTTING'

if guess == correct_password:
    success_or_failure = ['EXITING DEBUG MODE', '',
                          'LOGIN SUCCESSFUL - WELCOME BACK', '',
                          'PRESS ENTER TO CONTINUE']
else:
    success_or_failure = ['LOGIN FAILURE - TERMINAL LOCKED', '',
                          'PLEASE CONTACT AN ADMINISTRATOR', '',
                          'PRESS ENTER TO EXIT']

# DISPLAY OUTCOME
line_y = (window.get_height() - 7 * string_height) // 2

for outcome_line in [guess] + success_or_failure:
    x_space = window.get_width() - window.get_string_width(outcome_line)
    line_x = x_space // 2
    window.draw_string(outcome_line, line_x, line_y)
    window.update()
    sleep(0.5)
    line_y = line_y + string_height



# CLOSE WINDOW
window.close()
