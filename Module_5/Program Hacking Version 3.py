from uagame import Window
from time import sleep
#create window
window = Window('Hacking',600,500)
window.set_font_name('couriernew')
window.set_font_size(18)
window.set_font_color('green')
window.set_bg_color('black')

#GAME START
string_height = window.get_font_height()
line_y = 0

window.draw_string('DEBUG MODE',0,0)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('1 ATTEMPT(S) LEFT',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('',0,line_y)
window.update()
sleep(0.5)

#PASSWORD
line_y = line_y + string_height

window.draw_string('PROVIDE',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('SETTING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('CANTINA',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height


window.draw_string('CUTTING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('HUNTERS',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('SURVIVE',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('HEARING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('HUNTING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('REALIZE',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('NOTHING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('OVERLAP',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('FINDING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('PUTTING',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height

window.draw_string('',0,line_y)
window.update()
sleep(0.5)
line_y = line_y + string_height


C = 'PUTTING'


#GUESS
guess = window.input_string("ENTER PASSWAORD >",0,line_y)


#to diplay in the center
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2

outcome_height = 7*string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2

#END THE GAME
window.clear()
window.update()

#check the guess

if guess == C:
        outcome_line2 = 'EXITING DEBUG MODE'
        outcome_line3 = 'LOGIN SUCCESSFUL - WELCOME BACK'
        prompt = 'PRESS ENTER TO CONTINUE'
else:
        # create failure
        outcome_line2 = 'LOGIN FAILURE - TERMINAL LOCKED'
        outcome_line3 = 'PLEASE CONTACT AN ADMINISTRATOR'
        prompt = 'PRESS ENTER TO EXIT'
            
    #   display outcome
    #      display guess
    #         compute x coordinate
x_space = window.get_width() - window.get_string_width(guess)
line_x = x_space // 2
    
    #         compute y coordinate
outcome_height = 7*string_height
y_space = window.get_height() - outcome_height
line_y = y_space // 2
    
window.draw_string(guess, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height   
        
    #      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
    
    #      display outcome line 2
    #         compute x coordinate
x_space = window.get_width() - window.get_string_width(outcome_line2)
line_x = x_space // 2
window.draw_string(outcome_line2, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height   
    
    #      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
    
    #      display outcome line 3
    #         compute x coordinate
x_space = window.get_width() - window.get_string_width(outcome_line3)
line_x = x_space // 2
window.draw_string(outcome_line3, line_x, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height   
        
    #      display blank line
window.draw_string('', 0, line_y)
window.update()
sleep(0.3)
line_y = line_y + string_height
    
    #   prompt for end
    #      compute x coordinate
x_space = window.get_width() - window.get_string_width(prompt)
line_x = x_space // 2
window.input_string(prompt, line_x, line_y)
    
    #   close window
window.close()
