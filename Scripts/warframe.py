import time
import keyboard
import threading
import pyttsx3


threads = []
engine = pyttsx3.init()


# -----
# Flags
# -----

#? Add global flags here 
break_afk_move_flag = False
limbo_flag = False


# ---------
# Functions
# ---------
# Every new hotkey should have a set global flag
# and the function itself
def set_global_afk_move_flag(state: bool):
  global break_afk_move_flag
  break_afk_move_flag = state


#? Add new functions here
def afk_move():
  global break_afk_move_flag

  while True:
    if break_afk_move_flag == True:
      return False
    
    time.sleep(1)
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')
    keyboard.press('w')
    time.sleep(1.1)
    keyboard.release('w')


def limbo():
  global break_afk_move_flag

  while True:
    if break_afk_move_flag == True:
      return False
    
    time.sleep(1)
    keyboard.press('s')
    time.sleep(1)
    keyboard.release('s')
    keyboard.press('w')
    time.sleep(1.1)
    keyboard.release('w')


# ----
# Maps
# ----
# Extend all functions inside here
thread_name_fn_map = {
  'afk_move': afk_move
}

thread_name_flag_map = {
  'afk_move': set_global_afk_move_flag
}


# ---------
# Threading
# ---------
def start_thread(thread_name: str):
  global threads
  
  for thread in enumerate(threads):
    if thread.getName() == thread_name:
      return

  thread_name_flag_map[thread_name](False)

  afk_move_thread = threading.Thread(target=thread_name_fn_map[thread_name])
  afk_move_thread.setName(thread_name)
  afk_move_thread.start()
  
  threads.append(afk_move_thread)

  print("Started thread: " + thread_name)
  engine.say("Started thread: " + thread_name)
  

def stop_thread(thread_name: str):
  global threads

  thread_name_flag_map[thread_name](True)

  for index, thread in enumerate(threads):
    if thread.getName() == thread_name:
      thread.join()
      threads.pop(index)

  print("Stopped thread: " + thread_name)
  engine.say("Stopped thread: " + thread_name)


# 59 - f1
# 60 - f2

# -------
# Hotkeys
# -------
keyboard.add_hotkey(59, start_thread, args=['afk_move'])
keyboard.add_hotkey(60, stop_thread, args=['afk_move'])

keyboard.wait()