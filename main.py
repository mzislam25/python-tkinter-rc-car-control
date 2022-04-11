import serial
import time
import tkinter


def quit():
    global tkTop
    tkTop.destroy()


def writeData(s):
    try:
        varLabel.set("Command: "+s)
        ser.write(bytes(s, 'UTF-8'))
    except Exception as e:
        print(e)

def keyPress(event):
    # print(event)
    if event.keysym == 'w' or event.keysym == 'W':
        writeData('F')
    if event.keysym == 's' or event.keysym == 'S':
        writeData('B')
    if event.keysym == 'a' or event.keysym == 'A':
        writeData('L')
    if event.keysym == 'd' or event.keysym == 'D':
        writeData('R')
    if event.keysym == 'space':
        writeData('S')
    if event.keysym == 'Escape':
        if ser.is_open:
            ser.close()
        tkTop.destroy()

        

tkTop = tkinter.Tk()
tkTop.geometry('600x400')
tkTop.title("Arduino rc car control gui")

tkTop.bind('<w>', keyPress)
tkTop.bind('<s>', keyPress)
tkTop.bind('<a>', keyPress)
tkTop.bind('<d>', keyPress)
tkTop.bind('<space>', keyPress)
tkTop.bind('<Escape>', keyPress)

varLabel = tkinter.StringVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack(side="bottom")

f = open("port.txt", "r")
ser = serial.Serial(f.read(), 9600)
print("Connected to arduino on port "+ser.name)
time.sleep(3)
writeData('S')

buttonForward = tkinter.IntVar()
buttonForwardState = tkinter.Button(tkTop,
    text="Forward",
    command=lambda: writeData('F'),
    height = 2,
    fg = "black",
    width = 8,
    bd = 3,
    activebackground='green'
)
buttonForwardState.pack(side='top', ipadx=10, padx=10, pady=15)

buttonBackward = tkinter.IntVar()
buttonBackwardState = tkinter.Button(tkTop,
    text="Backward",
    command=lambda: writeData('B'),
    height = 2,
    fg = "black",
    width = 8,
    bd = 3,
    activebackground='green'
)
buttonBackwardState.pack(side='bottom', ipadx=10, padx=10, pady=60)

buttonLeft = tkinter.IntVar()
buttonLeftState = tkinter.Button(tkTop,
    text="Left",
    command=lambda: writeData('L'),
    height = 2,
    fg = "black",
    width = 8,
    bd = 3,
    activebackground='green'
)
buttonLeftState.pack(side='left', ipadx=10, padx=10, pady=15)

buttonRight = tkinter.IntVar()
buttonRightState = tkinter.Button(tkTop,
    text="Right",
    command=lambda: writeData('R'),
    height = 2,
    fg = "black",
    width = 8,
    bd = 3,
    activebackground='green'
)
buttonRightState.pack(side='right', ipadx=10, padx=10, pady=15)

buttonStop = tkinter.IntVar()
buttonStopState = tkinter.Button(tkTop,
    text="Stop",
    command=lambda: writeData('S'),
    height = 2,
    fg = "black",
    width = 8,
    bd = 3,
    activebackground='green'
)
buttonStopState.pack(side='bottom', ipadx=10, padx=10, pady=15)



# tkButtonQuit = tkinter.Button(
#     tkTop,
#     text="Quit",
#     command=quit,
#     height = 4,
#     fg = "black",
#     width = 8,
#     bg = 'yellow',
#     bd = 5
# )
# tkButtonQuit.pack(side='bottom', ipadx=10, padx=10, pady=15)

tkinter.mainloop()
