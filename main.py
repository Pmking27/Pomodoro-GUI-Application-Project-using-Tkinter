from tkinter import *
import math
import ttkthemes
from tkinter import ttk


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
resp=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer(): 
    reset.config(state=DISABLED)
    start.config(state=NORMAL)
    global timer
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
    check_maker.config(text="")
    global resp
    resp=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    start.config(state=DISABLED)
    reset.config(state=NORMAL)
    global resp
    resp+=1
    work_sec=WORK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60

    if resp % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif resp % 2 ==0:    
        count_down(short_break_sec)
        timer_label.config(text="Break",fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
 
def count_down(count):
    count_min=math.floor(count/60)
    count_sec= count % 60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()   
        marks=""
        work_sessions = math.floor(resp/2)
        for _ in range (work_sessions):
            marks += "✔"
        check_maker.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

window = ttkthemes.ThemedTk()
window.get_themes()
window.set_theme('radiance')
window.title("Pomodoro")
window.iconbitmap(r'tomato_icon.ico')
window.config(padx=100,pady=50,bg=YELLOW)

timer_label=Label(text="Timer" ,bg = YELLOW ,fg = GREEN ,font = (FONT_NAME,50))
timer_label.grid(column=2,row=1)

check_maker=Label(text="",bg=YELLOW,fg=GREEN)
check_maker.grid(column=2,row=3)

start=ttk.Button(text="Start",command = start_timer)
start.grid(column=0,row=3)

reset=ttk.Button(text="Reset",command=reset_timer)
reset.grid(column=3,row=3)
reset.config(state=DISABLED)


canvas=Canvas(width=210,height=250,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(104,120,image=photo)
canvas.grid(column=2,row=2)
timer_text=canvas.create_text(104,140,text="00:00",fill="White",font=(FONT_NAME,35,"bold"))

window.mainloop()
