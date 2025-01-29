from tkinter import Tk, Label, Button

root = Tk() # create a window
Label(root, text="Welcome").pack() # create a label
Button(root, text="Click me!" , command = lambda: print("Hello!")).pack() # create a button
root.mainloop() # run the window