from tkinter import *
import tkinter.font as font
import random
root = Tk()
root.geometry("700x300")
root.title("rock paper scissors")

l1_font = font.Font(size = 20)

l1 = Label(root, text = "rock paper scissors", fg="light gray", font=(l1_font))
l1.pack()

l2 = Label(root, text = "lets play a game...😈", fg="black")
l2.pack()

frame = Frame(root)
frame.pack()

options = Label(frame, text="options: ")
options.grid(row=1, column=1, padx=8, pady=5)

rock = Button(frame, text="🗿", bg="gray")
rock.grid(row=1, column=2, padx=8, pady=5)

paper = Button(frame, text="📄")
paper.grid(row=1, column=3, padx=8, pady=5)

scissors = Button(frame, text="✂️", bg="silver")
scissors.grid(row=1, column=4, padx=8, pady=5)

pchoice = Label(frame, text="you selected: " )
pchoice.grid(row=2, column=1, padx=8, pady=5)

cchoice = Label(frame, text="computer selected: ")
cchoice.grid(row=3, column=1, padx=8, pady=5)

pscore = Label(frame, text="your score: ")
pscore.grid(row=2, column=3, padx=8, pady=5)

cscore = Label(frame, text="computer score: ")
cscore.grid(row=3, column=3, padx=8, pady=5)

root.mainloop()
