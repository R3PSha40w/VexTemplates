#include "vex.h"

using namespace vex;

vex::brain       Brain;

/* This button class makes drawing buttons easier.
It gives basic `checkPress`, `draw`, and `isPressed`
functions so that the user can interact with buttons
on the Brain screen. */
class Button {
public:
  int x, y, w, h;
  const char* label;
  bool _pressed_last = false;

  Button(int x, int y, int w, int h, const char* label)
      : x(x), y(y), w(w), h(h), label(label) {}

  void draw() {
    Brain.Screen.setPenColor(white);
    Brain.Screen.drawRectangle(x, y, w, h);
    Brain.Screen.setCursor((y / 20) + 1, (x / 10) + 1);
    Brain.Screen.print(label);
  }

  bool isPressed(int tx, int ty) {
    return tx >= x && tx <= x + w && ty >= y && ty <= y + h;
  }

  bool checkPress() {
    if (Brain.Screen.pressing()) {
      int tx = Brain.Screen.xPosition();
      int ty = Brain.Screen.yPosition();
      if (isPressed(tx, ty)) {
        if (!_pressed_last) {
          _pressed_last = true;
          return true;
        }
      }
    } else {
      _pressed_last = false;
    }
    return false;
  }
};

/* === Simple Example ===

This is a sample of what you can do with this class and template.
First, it creates the button variables. Then in the main loop,
it clears the screen and draws the first button. After that it
goes into a loop where if one of the buttons are pressed it
clears the screen and draws a different progress (button). */
Button sbutton1(100, 100, 100, 40, "Start");
Button sbutton2(100, 100, 100, 40, "End");

void simple_example() {
  bool showingStart = true;
  Brain.Screen.clearScreen();
  sbutton1.draw();

  while (true) {
    if (showingStart && sbutton1.checkPress()) {
      showingStart = false;
      Brain.Screen.clearScreen();
      sbutton2.draw();
    }

    if (!showingStart && sbutton2.checkPress()) {
      showingStart = true;
      Brain.Screen.clearScreen();
      sbutton1.draw();
    }

    wait(20, msec);
  }
}

/* === Multi-Layer Menu Example ===

One of the things that you can do with this is create layers of buttons.
With the layers you can create menus inside of menus for however long
that you want. This is an example of a multilayer of buttons.

This program creates a settings menu and when the setting button is pressed,
it shows 3 more buttons. When one of those 3 buttons are pressed it clears
the screen and then shows a back button. When the back button is clicked it
goes back to the page with 3 buttons. */

Button mbutton1(0, 0, 80, 40, "Settings");
Button mbutton2(80, 100, 80, 40, "SC");     // SC: Screen Color
Button mbutton3(200, 100, 80, 40, "PS");    // PS: Pen Size
Button mbutton4(320, 100, 80, 40, "Debug");
Button mbutton5(150, 200, 80, 40, "Back");

enum State {
  MAIN_MENU,
  OPTIONS_MENU,
  SUBMENU_SC,
  SUBMENU_PS,
  SUBMENU_DBG
};

void multi_layer_example() {
  State currentState = MAIN_MENU;
  Brain.Screen.clearScreen();
  mbutton1.draw();

  while (true) {
    switch (currentState) {
      case MAIN_MENU:
        if (mbutton1.checkPress()) {
          currentState = OPTIONS_MENU;
          Brain.Screen.clearScreen();
          mbutton2.draw();
          mbutton3.draw();
          mbutton4.draw();
        }
        break;

      case OPTIONS_MENU:
        if (mbutton2.checkPress()) {
          currentState = SUBMENU_SC;
          Brain.Screen.clearScreen();
          mbutton5.draw();
        }
        if (mbutton3.checkPress()) {
          currentState = SUBMENU_PS;
          Brain.Screen.clearScreen();
          mbutton5.draw();
        }
        if (mbutton4.checkPress()) {
          currentState = SUBMENU_DBG;
          Brain.Screen.clearScreen();
          mbutton5.draw();
        }
        break;

      case SUBMENU_SC:
      case SUBMENU_PS:
      case SUBMENU_DBG:
        if (mbutton5.checkPress()) {
          currentState = OPTIONS_MENU;
          Brain.Screen.clearScreen();
          mbutton2.draw();
          mbutton3.draw();
          mbutton4.draw();
        }
        break;
    }

    wait(20, msec);
  }
}

/* === Entry Point === 
Choose which example you want to run by uncommenting it: 
  simple_example();    // A single-button toggle demo
  multi_layer_example(); // A layered GUI menu example 
*/

int main() {
  // Run either of the following:
    //simple_example();
    multi_layer_example();

  return 0;
}
