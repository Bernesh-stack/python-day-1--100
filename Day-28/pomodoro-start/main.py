import tkinter
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
    count_Down(5*60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_Down(count):
    ount_min = math.floor(count/60)
    count_ec = count%60
    Canvas.itemconfig(Timer_test,test=count)
    if count>0:
        window.after(1000, count_Down, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("palindrome")
window.config(padx=100,pady=50,bg=YELLOW)






Canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
Canvas.create_image(100,112,image=tomato_img)
Timer_test = Canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
head = tkinter.Label(text="Timer",fg=GREEN,highlightthickness=0,bg=YELLOW,font=(FONT_NAME,50))
count_Down(count=5)


st_btn = tkinter.Button(text="Start",command=start_timer)
reset_btn = tkinter.Button(text="reset",highlightthickness=0,bg=YELLOW)
Check_mark = tkinter.Label(text="✅", highlightthickness=0,bg=YELLOW)
head.grid(row=0,column=1)
Canvas.grid(row=1,column=1)
st_btn.grid(row=2,column=0)
reset_btn.grid(row=2,column=2)
Check_mark.grid(row=2,column=1)









window.mainloop()
