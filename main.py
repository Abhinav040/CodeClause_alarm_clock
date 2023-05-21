from tkinter import *
from tkinter import messagebox
import time
from pygame import mixer

root=Tk()
root.geometry("320x230")
root.title("Alarm Clock")

alarmtime = StringVar()
messagein = StringVar()

mixer.init()

def al():
    given = alarmtime.get()
    if given == "":
        alert = messagebox.showerror('Invalid data','Please enter valid time')
    else:
        alTime= given
        currentTime = time.strftime("%H:%M")
        
        while alTime != currentTime:
            currentTime = time.strftime("%H:%M")
        
        if alTime == currentTime:
            mixer.music.load('sound.mp3')
            mixer.music.play()
            alert = messagebox.showinfo('Time Up',f'{messagein.get()}')
            if alert == 'ok':
                mixer.music.stop()



    

#main
heading=Label(root,text="Alarm Clock ",font=('comic sans',18),bg="yellow").grid(row=0,columnspan=3,pady=10)

input = Label(root,text="Enter Time:(HH:MM) ",font="comicsans 14")
input.grid(row=1,column=1,pady=10)

timeT= Entry(root,font="comicsans 16",width=6,textvariable=alarmtime)
timeT.grid(row=1,column=2)

msg = Label(root,text="Message ",font="comicsans 13").grid(row=2,column=1,columnspan=2,pady=5)

msginput = Entry(root,font="comicsans 16",textvariable=messagein).grid(row=3,column=1,columnspan=2,padx=10,pady=10)

submit = Button(root, text="Submit",font="comicsans 10",command=al).grid(row=4,column=1,columnspan=2)



root.mainloop()