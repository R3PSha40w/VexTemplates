# Library imports
from vex import *

brain = Brain()

""" This button class lets you create and customize buttons. It also lets you be able to 
detect presses and from that be able to control or initiate something. """
class Button:
    def __init__(self, x, y, width, height, label, outline_color=Color.WHITE, text_color=Color.WHITE, gap=0, outsideLabel=""):
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.g = gap
        self.label = label
        self.Olabel = outsideLabel
        self.outline_color = outline_color
        self.text_color = text_color
        self._pressed_last = False

    def draw(self):
        # Draw the button rectangle
        brain.screen.set_pen_color(self.outline_color)
        brain.screen.draw_rectangle(self.x, self.y, self.w, self.h)

        # Draw the inside label (centered)
        char_width = 6
        char_height = 10
        text_width = len(self.label) * char_width
        text_height = char_height

        text_x = self.x + (self.w - text_width) // 2
        text_y = self.y + (self.h - text_height) // 2

        brain.screen.set_pen_color(self.text_color)
        brain.screen.print_at(self.label, text_x, text_y)

        # Draw the outside label (horizontally aligned with button center)
        if self.Olabel:
            outside_text_width = len(self.Olabel) * char_width
            outside_text_height = char_height

            outside_y = self.y + (self.h - outside_text_height) // 2

            # Place the outside label to the right or left depending on gap
            if self.g >= 0:
                outside_x = self.x + self.w + self.g
            else:
                outside_x = self.x + self.g - outside_text_width  # Adjust for text width when on left

            brain.screen.print_at(self.Olabel, outside_x, outside_y)

    def is_pressed(self, touch_x, touch_y):
        return (self.x <= touch_x <= self.x + self.w and
                self.y <= touch_y <= self.y + self.h)

    def check_press(self):
        if brain.screen.pressing():
            x = brain.screen.x_position()
            y = brain.screen.y_position()
            if self.is_pressed(x, y):
                if not self._pressed_last:
                    self._pressed_last = True
                    return True
            else:
                self._pressed_last = False
        else:
            self._pressed_last = False
        return False

""" The complex example starts here"""

#The complex example is taken straight from my code
settingsDisplayed = False
autonDisplayed = False
speedDisplayed = False
debugMode = False
auto = 0
speed_multiplier = 1
settingsMenu = Button(0, 0, 80, 40, "Settings", Color.WHITE, Color.WHITE)
autonMenu = Button(80, 100, 80, 40, "Auto", Color.WHITE, Color.WHITE, gap=0, outsideLabel=f"{auto}")
speedMenu = Button(200, 100, 80, 40, "Speed", Color.WHITE, Color.WHITE, gap=0, outsideLabel=f"{speed_multiplier}")
debugBTN = Button(320, 100, 80, 40, "Debug", Color.WHITE, Color.WHITE)
backBTN = Button(0, 0, 80, 40, "Back", Color.WHITE, Color.WHITE)
LSQ = Button(80, 60, 80, 40, "LSQ", Color.WHITE, Color.WHITE)
RSQ = Button(200, 60, 80, 40, "RSQ", Color.WHITE, Color.WHITE)
LSE = Button(320, 60, 80, 40, "LSE", Color.WHITE, Color.WHITE)
RSE = Button(140, 140, 80, 40, "RSE", Color.WHITE, Color.WHITE)
SKL = Button(260, 140, 80, 40, "SKL", Color.WHITE, Color.WHITE)
point5 = Button(56, 100, 80, 40, "0.5", Color.WHITE, Color.WHITE)
one = Button(152, 100, 80, 40, "1", Color.WHITE, Color.WHITE)
onePoint5 = Button(248, 100, 80, 40, "1.5", Color.WHITE, Color.WHITE)
two = Button(344, 100, 80, 40, "2", Color.WHITE, Color.WHITE)


def settings_Menu():
    global settingsDisplayed
    if settingsMenu.check_press():
        settingsDisplayed = True
        brain.screen.clear_screen()
        autonMenu.draw()
        speedMenu.draw()
        debugBTN.draw()
        backBTN.draw()

def auton_Menu():
    global autonDisplayed
    if autonMenu.check_press() and settingsDisplayed:
        autonDisplayed = True
        brain.screen.clear_screen()
        backBTN.draw()
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

def select_Auton():
    global auto, autonDisplayed, settingsDisplayed, LSQ, RSQ, RSE, LSE, SKL
    if autonDisplayed and settingsDisplayed and LSQ.check_press():
        auto = 2
        LSQ = Button(80, 60, 80, 40, "LSQ", Color.GREEN, Color.GREEN)
        brain.screen.clear_screen()
        RSQ = Button(200, 60, 80, 40, "RSQ", Color.WHITE, Color.WHITE)
        LSE = Button(320, 60, 80, 40, "LSE", Color.WHITE, Color.WHITE)
        RSE = Button(140, 140, 80, 40, "RSE", Color.WHITE, Color.WHITE)
        SKL = Button(260, 140, 80, 40, "SKL", Color.WHITE, Color.WHITE)
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

    if autonDisplayed and settingsDisplayed and RSQ.check_press():
        auto = 1
        RSQ = Button(200, 60, 80, 40, "RSQ", Color.GREEN, Color.GREEN)
        brain.screen.clear_screen()
        LSQ = Button(80, 60, 80, 40, "LSQ", Color.WHITE, Color.WHITE)
        LSE = Button(320, 60, 80, 40, "LSE", Color.WHITE, Color.WHITE)
        RSE = Button(140, 140, 80, 40, "RSE", Color.WHITE, Color.WHITE)
        SKL = Button(260, 140, 80, 40, "SKL", Color.WHITE, Color.WHITE)
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

    if autonDisplayed and settingsDisplayed and LSE.check_press():
        auto = 4
        LSE = Button(320, 60, 80, 40, "LSE", Color.GREEN, Color.GREEN)
        brain.screen.clear_screen()
        LSQ = Button(80, 60, 80, 40, "LSQ", Color.WHITE, Color.WHITE)
        RSQ = Button(200, 60, 80, 40, "RSQ", Color.WHITE, Color.WHITE)
        RSE = Button(140, 140, 80, 40, "RSE", Color.WHITE, Color.WHITE)
        SKL = Button(260, 140, 80, 40, "SKL", Color.WHITE, Color.WHITE)
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

    if autonDisplayed and settingsDisplayed and RSE.check_press():
        auto = 3
        RSE = Button(140, 140, 80, 40, "RSE", Color.GREEN, Color.GREEN)
        brain.screen.clear_screen()
        LSQ = Button(80, 60, 80, 40, "LSQ", Color.WHITE, Color.WHITE)
        RSQ = Button(200, 60, 80, 40, "RSQ", Color.WHITE, Color.WHITE)
        LSE = Button(320, 60, 80, 40, "LSE", Color.WHITE, Color.WHITE)
        SKL = Button(260, 140, 80, 40, "SKL", Color.WHITE, Color.WHITE)
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

    if autonDisplayed and settingsDisplayed and SKL.check_press():
        auto = 5
        SKL = Button(260, 140, 80, 40, "SKL", Color.GREEN, Color.GREEN)
        brain.screen.clear_screen()
        LSQ = Button(80, 60, 80, 40, "LSQ", Color.WHITE, Color.WHITE)
        RSQ = Button(200, 60, 80, 40, "RSQ", Color.WHITE, Color.WHITE)
        LSE = Button(320, 60, 80, 40, "LSE", Color.WHITE, Color.WHITE)
        RSE = Button(140, 140, 80, 40, "RSE", Color.WHITE, Color.WHITE)
        LSQ.draw()
        LSE.draw()
        RSE.draw()
        RSQ.draw()
        SKL.draw()

def speed_Menu():
    global speedDisplayed, speed_multiplier
    if speedMenu.check_press() and settingsDisplayed:
        speedDisplayed = True
        brain.screen.clear_screen()
        backBTN.draw()
        point5.draw()
        one.draw()
        onePoint5.draw()
        two.draw()

def speed_Select():
    global settingsDisplayed, speedDisplayed, one, two, onePoint5, point5, speed_multiplier
    if speedDisplayed and settingsDisplayed and point5.check_press():
        speed_multiplier = 0.5
        brain.screen.clear_screen()
        point5 = Button(56, 100, 80, 40, "0.5", Color.GREEN, Color.GREEN)
        one = Button(152, 100, 80, 40, "1", Color.WHITE, Color.WHITE)
        onePoint5 = Button(248, 100, 80, 40, "1.5", Color.WHITE, Color.WHITE)
        two = Button(344, 100, 80, 40, "2", Color.WHITE, Color.WHITE)
        point5.draw()
        one.draw()
        two.draw()
        onePoint5.draw()
        backBTN.draw()

    if speedDisplayed and settingsDisplayed and one.check_press():
        speed_multiplier = 1.0
        brain.screen.clear_screen()
        point5 = Button(56, 100, 80, 40, "0.5", Color.WHITE, Color.WHITE)
        one = Button(152, 100, 80, 40, "1", Color.GREEN, Color.GREEN)
        onePoint5 = Button(248, 100, 80, 40, "1.5", Color.WHITE, Color.WHITE)
        two = Button(344, 100, 80, 40, "2", Color.WHITE, Color.WHITE)
        point5.draw()
        one.draw()
        two.draw()
        onePoint5.draw()
        backBTN.draw()
    
    if speedDisplayed and settingsDisplayed and onePoint5.check_press():
        speed_multiplier = 1.5
        brain.screen.clear_screen()
        point5 = Button(56, 100, 80, 40, "0.5", Color.WHITE, Color.WHITE)
        one = Button(152, 100, 80, 40, "1", Color.WHITE, Color.WHITE)
        onePoint5 = Button(248, 100, 80, 40, "1.5", Color.GREEN, Color.GREEN)
        two = Button(344, 100, 80, 40, "2", Color.WHITE, Color.WHITE)
        point5.draw()
        one.draw()
        two.draw()
        onePoint5.draw()
        backBTN.draw()
    
    if speedDisplayed and settingsDisplayed and point5.check_press():
        speed_multiplier = 0.5
        brain.screen.clear_screen()
        point5 = Button(56, 100, 80, 40, "0.5", Color.WHITE, Color.WHITE)
        one = Button(152, 100, 80, 40, "1", Color.WHITE, Color.WHITE)
        onePoint5 = Button(248, 100, 80, 40, "1.5", Color.WHITE, Color.WHITE)
        two = Button(344, 100, 80, 40, "2", Color.GREEN, Color.GREEN)
        point5.draw()
        one.draw()
        two.draw()
        onePoint5.draw()
        backBTN.draw()

def debug_Mode():
    global debugMode, debugBTN
    if debugBTN.check_press() and settingsDisplayed:
        if debugMode == False:
            debugMode = True
            brain.screen.clear_screen()
            debugBTN = Button(320, 120, 80, 40, "Debug", Color.GREEN, Color.GREEN)
            debugBTN.draw()
            autonMenu.draw()
            speedMenu.draw()

        if debugMode == True:
            debugMode = False
            brain.screen.clear_screen()
            debugBTN = Button(320, 120, 80, 40, "Debug", Color.WHITE, Color.WHITE)
            debugBTN.draw()
            autonMenu.draw()
            speedMenu.draw()
    
def back_Button():
    global settingsDisplayed, autonDisplayed, speedDisplayed
    if settingsDisplayed and backBTN.check_press():
        settingsDisplayed = False
        brain.screen.clear_screen()

    if settingsDisplayed and autonDisplayed and backBTN.check_press():
        autonDisplayed = False
        settingsDisplayed = True
        brain.screen.clear_screen()
        autonMenu.draw()
        speedMenu.draw()
        debugBTN.draw()
        backBTN.draw()

    if settingsDisplayed and speedDisplayed and backBTN.check_press():
        speedDisplayed = False
        settingsDisplayed = True
        brain.screen.clear_screen()
        autonMenu.draw()
        speedMenu.draw()
        debugBTN.draw()
        backBTN.draw()

def when_Started():
    while True:
        settings_Menu()
        auton_Menu()
        speed_Menu()
        debug_Mode()
        back_Button()
        select_Auton()

def autonomous():
    pass

def user_control():
    pass

comp = Competition(user_control, autonomous)

brain.screen.clear_screen()