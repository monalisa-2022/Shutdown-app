from tkinter import *
import subprocess

def restart():
   subprocess.Popen(["shutdown" , "/r"," /t"," 30"])
def restart_time():
   subprocess.Popen(["shutdown", "/r", "/t", "20"])
def logout():
    subprocess.Popen(["shutdown", "-1"])
def shutdown():
    subprocess.Popen(["shutdown"," /s", "/t", "1"])

st=Tk()
st.title("SHUTDOWN APP")
st.geometry("500x500")
st.config(bg="purple")
button=Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart)
button.place(x=150,y=60,height=50,width=200)

button_1=Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=restart_time)
button_1.place(x=150,y=170,height=50,width=200)

button_2=Button(st,text="LOG OUT",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=logout)
button_2.place(x=150,y=270,height=50,width=200)

button_3=Button(st,text="SHUT DOWN",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="plus",command=shutdown)
button_3.place(x=150,y=370,height=50,width=200)

st.mainloop()