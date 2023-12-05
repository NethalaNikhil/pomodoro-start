from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    count_down(5 * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    In_min = math.floor(count / 60)
    In_sec = count % 60
    canvas.itemconfig(timer_text, text=f"{In_min}:{In_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100, pady=50, background=YELLOW)

canvas = Canvas(width=200, height=224)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.config(bg=YELLOW, highlightthickness=0)

label_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
label_text.grid(column=1, row=0)
start_button = Button(text="start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="reset", highlightthickness=0)
reset_button.grid(column=2, row=2)
check_box = Label(text="✓", fg=GREEN, bg=YELLOW)
check_box.grid(column=1, row=3)
canvas.grid(column=1, row=1)

window.mainloop()
