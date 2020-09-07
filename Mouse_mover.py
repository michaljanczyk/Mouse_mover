import pyautogui, time
from pynput import keyboard

# ---------------------------------VARIABLES-----------------------------------

pyautogui.FAILSAFE = False # wychodzenie za ekran
move_duration = 0.25    # seconds
distance_diff = 5       # px
defined_distance = 500
pause = False
elapsed_time = 0

# ---------------------------------FUNCTIONS-----------------------------------

def move(distance):
    # start_time = time.time()
    while distance > 0:
        if(pause):
            time.sleep(0.1) # mniejsze CPU usage
        else:
            start_time = time.time()
            pyautogui.moveRel(distance, 0, move_duration)   # move right
            distance = distance - distance_diff
            pyautogui.moveRel(0, distance, move_duration)   # move down
            pyautogui.moveRel(-distance, 0, move_duration)  # move left
            distance = distance - distance_diff
            pyautogui.moveRel(0, -distance, move_duration)  # move up
            iteration_time = time.time() - start_time
            global elapsed_time
            elapsed_time += iteration_time
            if((distance % 50) == 0):
                print("Minęło ", "%.2f" % elapsed_time, " sekund")
            pyautogui.press(['left', 'right', 'left', 'right'])

def on_press(key):
    try:
        if (key == keyboard.Key.esc):
            global pause
            pause = not pause
            print("Pauza: ", pause)
    except AttributeError:
        print('invalid key {0} pressed'.format(key))

def key_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

# -----------------------------------MAIN--------------------------------------

key_listener()
while True:
    time.sleep(1)
    distance = defined_distance
    move(distance)
