import time

from pyautogui import click, displayMousePosition, typewrite, hotkey

#clicking the application icon
click(822, 852)
time.sleep(5)

#clicking the sign in button
click(693, 555)
time.sleep(5)

#entering password and pressing enter
click(622,152)
typewrite('Welcome2Mission!')
hotkey('enter')

#waiting for duo approval
time.sleep(20)

#clicking dragon and paragon after signing in
click(440, 361)
click(440, 361)
time.sleep(5)
click(248, 343)
time.sleep(3)