from tkinter import *
import math
from playsound import playsound
# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# Variables
reps = 0
timer = None

# Timer Mechanism
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        heading.config(text="LONG BREAK", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        heading.config(text="SHORT BREAK", fg=PINK)
    else:
        count_down(work_sec)
        heading.config(text="WORK", fg=GREEN)

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{count_min:02d}:{count_sec:02d}")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 1:
            playsound("beep.mp3")

# Timer Reset
def reset_timer():
    global reps
    reps = 0
    if timer:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    heading.config(text="TIMER", fg=GREEN)

# UI Setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

heading = Label(text="POMODORO TIMER", font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
heading.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=1)

start_button = Button(
    text="START",
    font=(FONT_NAME, 17),
    bg=YELLOW,
    fg=GREEN,
    relief=FLAT,
    padx=20,
    pady=10,
    highlightthickness=0,
    borderwidth=0,
    command=start_timer,
)
start_button.grid(column=0, row=3)

reset_button = Button(
    text="RESET",
    font=(FONT_NAME, 17),
    bg=YELLOW,
    fg=GREEN,
    relief=FLAT,
    padx=20,
    pady=10,
    highlightthickness=0,
    borderwidth=0,
    activebackground=PINK,
    command=reset_timer,
)
reset_button.grid(column=3, row=3)

window.mainloop()
