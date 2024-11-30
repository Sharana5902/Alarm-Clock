from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import pygame
import threading

#initialize pygame
pygame.mixer.init()

play = False

# # store the sound
alarm_sound = pygame.mixer.Sound('alarm_sound.wav')

# create widgets
def createWidgets():

    label1 = Label(frame1, text="Enter the time in the format HH:MM -")
    label1.grid(row=0, column=0, padx=5, pady= 5)

    global entry1
    entry1 = Entry(frame1, width=20)
    entry1.grid(row=0, column=1, padx=5, pady=5)

    label2 = Label(frame1, text="Enter the message for the alarm: ")
    label2.grid(row=1, column=0, padx=10, pady= 5)

    global entry2
    entry2 = Entry(frame1, width=20)
    entry2.grid(row=1, column=1,  padx=10, pady=5)

    global label3
    label3 = Label(frame3, text="")
    label3.grid(row=0)

    global dismiss_button
    dismiss_button = ttk.Button(frame2, text="Dismiss", width=10, command=dismiss, state="disabled", style='fun.TButton')
    dismiss_button.grid(row=0, column=0, padx=5)

    global snooze_button
    snooze_button = ttk.Button(frame2, text="Snooze", command=snooze_alarm, state="disabled")
    snooze_button.grid(row=0,column=1,padx=5)

    button = ttk.Button(frame1, text="Submit", command=submit, width=10, style='NuclearReactor.TButton')
    button.grid(row=2,column=1,pady=5)

    
#funtion to dismiss the alarm
def dismiss():
    alarm_sound.stop()
    label3.config(text="ALARM DISMISSED.",foreground='red')

def snoozed():
    alarm_sound.play()
    label3.config(text=f"ALARM RINGING...")



#function to snooze for alarm
def snooze_alarm():
    def snooze():
        alarm_sound.stop()
        snoozing_time = snooze_time.get()
        label3.config(text=f"NEXT ALARM RINGS AFTER {snoozing_time} MINUTES")
        snooze_window.destroy()
        threading.Timer(snoozing_time*60, lambda: snoozed()).start()
       

    #Creating new snooze window
    snooze_window = tk.Toplevel(root)
    snooze_window.title("Snooze Options")
    snooze_window.geometry("200x200")

    snooze_time = tk.IntVar(value=2)

    radio_2 = ttk.Radiobutton(snooze_window, text="2 Min", variable=snooze_time, value=2)
    radio_2.grid(row=0, column=0, padx=5, pady=5)

    radio_5 = ttk.Radiobutton(snooze_window, text="5 Min", variable=snooze_time, value=5)
    radio_5.grid(row=1, column=0,padx=5, pady=5)

    radio_10 = ttk.Radiobutton(snooze_window, text="10 Min", variable=snooze_time, value=10)
    radio_10.grid(row=2,column=0,padx=5,pady=5)

    set_time_button = ttk.Button(snooze_window, text="snooze", command=snooze)
    set_time_button.grid(row=3, column=0, padx=5, pady=15)

def message1():
    global entry1, label3
    timeLabel = entry1.get()
    frame3.config(relief="sunken",borderwidth=5)
    label3.config(text="TIME IS TICKING...", foreground='black')
    messagebox.showinfo("Alarm Clock", f"Time is set to: {timeLabel}")
    

def submit():
    global entry1,entry2, label3
    alarm_time= entry1.get()
    alarm_message = entry2.get()
    message1()
    currenttime = time.strftime("%H:%M")
    
    while alarm_time != currenttime:
        currenttime = time.strftime("%H:%M") #fetches cuurent time every second 
        time.sleep(1)
    
    if alarm_time == currenttime:
        label3.config(text="THE ALARM IS RINGING...",foreground='green')
        
        alarm_sound.play()
        play = True
        messagebox.showinfo("Alarm Clock", f"Message: {alarm_message}")
        if play:
            dismiss_button.config(state='normal', command=dismiss)
            snooze_button.config(state='normal',command=snooze_alarm)
            
        
        
        

    
# create GUI

#creating root window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry('400x400')
root.resizable(False,False)

#creating frames
frame1 = ttk.Frame(root, padding=10, relief='raise', borderwidth=5)
frame1.grid(row=0, columnspan=2, rowspan=2,padx=5)
frame2 = ttk.Frame(root, padding=5)
frame2.grid(row=4, columnspan=2, rowspan=1)
frame3 = ttk.Frame(root, padding=5)
frame3.grid(row=2, columnspan=3, rowspan=1, pady=5)




createWidgets()

# run loop
root.mainloop()
