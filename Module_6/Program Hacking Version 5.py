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
line_x = 0
attempts_left = 4

header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']

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
prompt = 'ENTER PASSWORD >'

correct_password = 'PUTTING'

guess = ""

while guess == password and attempts_left > 0:
    guess = window.input_string(prompt, line_x, line_y)
    window.clear()
    line_y = 0
    
    if guess == correct_password:
        success_or_failure = ['EXITING DEBUG MODE', '',
                              'LOGIN SUCCESSFUL - WELCOME BACK', '',
                              'PRESS ENTER TO CONTINUE']
        break
    else:
        attempts_left -= 1
        if attempts_left > 0:
            header = ['DEBUG MODE', str(attempts_left) + ' ATTEMPT(S) LEFT', '']
            for header_line in header:
                window.draw_string(header_line, 0, line_y)
                line_y = line_y + string_height

            if attempts_left == 1:
                warning_string = '*** LOCKOUT WARNING ***'
                warning_x = window.get_width() - window.get_string_width(warning_string)
                warning_y = window.get_height() - string_height
                window.draw_string(warning_string, warning_x, warning_y)
            line_y += string_height

            for password in password_list:
                window.draw_string(password, 0, line_y)
                line_y = line_y + string_height

        else:
            success_or_failure = ['LOGIN FAILURE - TERMINAL LOCKED', '',
                                  'PLEASE CONTACT AN ADMINISTRATOR', '',
                                  'PRESS ENTER TO EXIT']
            break

    window.update()

# DISPLAY OUTCOME
window.clear()
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
