import pyautogui
import threading
import time
import tkinter as tk 
import keyboard  #install with: pip install keyboard

#State
clicking = False
click_count = 0

#Functions
def start_clicking():
    global clicking
    if not clicking:
        clicking = True
        status_label.config(text="Clicking... (press F6 or Stop to end)")
        thread = threading.Thread(target=auto_click)
        thread.daemon = True
        thread.start()

def stop_clicking():
    global clicking, click_count
    clicking = False
    click_count = 0
    counter_label.config(text="Clicks: 0")
    status_label.config(text="Stopped. (Counter reset)")

def auto_click():
    global click_count
    interval = float(interval_entry.get())
    time.sleep(1)
    while clicking:
        pyautogui.click()
        click_count += 1
        counter_label.config(text=f"Clicks: {click_count}")
        time.sleep(interval)

#Listener
def hotkey_listener():
    while True:
        keyboard.wait('f6')  #Key to toggle clicking
        if clicking:
            stop_clicking()
        else:
            start_clicking()

#UI
window = tk.Tk()
window.title("My AutoClicker")

window.geometry("500x350")
window.resizable(True, True)

tk.Label(window, text="Click interval (seconds):").pack(pady=10)
interval_entry = tk.Entry(window, font=("Arial", 12))
interval_entry.insert(0, "0.5")
interval_entry.pack(pady=5)

start_button = tk.Button(window, text="Start Clicking", command=start_clicking, bg="lightgreen", font=("Arial", 11))
start_button.pack(pady=5)

stop_button = tk.Button(window, text="Stop Clicking", command=stop_clicking, bg="salmon", font=("Arial", 11))
stop_button.pack(pady=5)

counter_label = tk.Label(window, text="Clicks: 0", font=("Arial", 12))
counter_label.pack(pady=10)

status_label = tk.Label(window, text="Press F6 or Start to begin.", font=("Arial", 10))
status_label.pack(pady=10)

threading.Thread(target=hotkey_listener, daemon=True).start()

window.mainloop()

#If you make any changes to the script and want to create an updated executable...
#You can use the following command (cmd) to package it with PyInstaller:
#python -m PyInstaller --noconsole --onefile MyAutoClicker.py