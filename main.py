import os
import time
import keyboard
import random

#TODO: Fix indentation with VSCode and other applications that auto-indent
    #  use a peek ahead to parse the number of indents and set cursor at beginning of line
    # probably

#TODO: Make the loop exiting statements actually work
    # No idea how to fix this yet
    # seems to be an issue caused by the keyboard.write attempting to input chars

def get_clipboard():
    command = 'powershell -command "Get-Clipboard"'
    process = os.popen(command)
    text = process.read()
    process.close()
    return text.strip()

def type_clipboard(text):
    max_value = 0.11
    min_value = .02
    place = 0
    # Simulate typing the text with rand-delay to appear more human-like
    
    while True:
        # Exit early with ctrl+f8
        if keyboard.is_pressed('ctrl+f8'):
            break
        
        keyboard.write(text[place], delay=random.uniform(min_value, max_value))
        place += 1
        if place >= len(text):
            break
        


def main():
    #will run until ctrl+f10 is pressed
    while True:
        if keyboard.is_pressed('ctrl+f10'):
            break
        
        elif keyboard.is_pressed('ctrl+f6'):
            clipboard_text = get_clipboard()
            if clipboard_text:
                type_clipboard(clipboard_text)
            else:
                print("Failed to get clipboard data.")
        
            

if __name__ == "__main__":
    main()
