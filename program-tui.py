import subprocess
import webview
import webbrowser
import tkinter as tk
import tkinter.font as font

from tkinter.ttk import *

command = ""
started = False
while True:
    print("""---------------------------------
    (1) Remove Activation text on Desktop       (6) Unlock Windows themes
    (2) Force DarkMode                          (7) Get free PC wallpapers
    (3) Force LightMode                         (8) Quit
    (4) Enable AutoColorization
    (5) Disable AutoColorization""")
    command = input("Choice: ").lower()
    if command =="about":
            print("""Unactivated Tweaker (TUI)
                  ------------------------------
                  Useful tools for unactivated Windows machines.""")
    elif command == "1":
        command = 'cmd /k bcdedit -set TESTSIGNING OFF'
        subprocess.Popen(command, shell=True)
        print("Activation text should be removed. Restart explorer.exe to see changes")
    elif command == "2":
        command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 0 /f"
        subprocess.Popen(command, shell=True)
        print("DarkMode should be applied.")
    elif command == "3":
        command = "reg add HKCU\Software\Microsoft\Windows\CurrentVersion\Themes\Personalize /v AppsUseLightTheme /t REG_DWORD /d 1 /f"
        subprocess.Popen(command, shell=True)
        print("LightMode should be applied.")
    elif command == "4":
        print("soon?")
    elif command == "5":
        print("soon?")
    elif command == "6":
        winThemeTut = tk.Tk()
        winThemeTut.title("Steps")
        winThemeTut.geometry("550x110")

        # widgets
        title = tk.Label(winThemeTut, text="How to change Windows theme")
        title.config(font=("Segoe UI", 14))
        title.pack()
        step1 = tk.Label(winThemeTut, text="1. Open Group Policy Editor")
        step1.config(font=("Segoe UI", 8))
        step1.pack()
        step2 = tk.Label(winThemeTut, text="2. Go to User Configuration > Administrative Templates > Control Panel > Personalization.")
        step2.config(font=("Segoe UI", 8))
        step2.pack()
        step3 = tk.Label(winThemeTut, text='3. Double-click "Prevent changing theme".')
        step3.config(font=("Segoe UI", 8))
        step3.pack()
        step4 = tk.Label(winThemeTut, text='4. Click on "Disabled" and click "OK".')
        step4.config(font=("Segoe UI", 8))
        step4.pack()
    elif command == "7":
        print("Opening pywebview window...")
        webview.create_window('Unsplash Wallpapers', 'https://unsplash.com/wallpapers/desktop')
        webview.start()
        print("Get free wallpapers at Unsplash (https://unsplash.com/)")
    elif command == "8":
        break
    else:
        print(f'Option "{command}" is invalid, buddy.')
