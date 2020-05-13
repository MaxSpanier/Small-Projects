from tkinter import *

def reverse():
    entered_text = textEntry.get()
    output.delete(0.0, END)
    reversed = entered_text[::-1]
    output.insert(END, reversed)

def close_window():
    window.destroy()
    exit()

window = Tk()

windowWidth = window.winfo_reqwidth()
windowHeight = window.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)

# window.geometry("250x150")
window.configure(bg="black")
window.resizable(True, True)
#Title
window.title("Reverse a string")
#Input label
Label(window, text="Enter a string you would like to reverse: ", bg="black", fg="white").grid(row=1, column=0, sticky=W)
#Input
textEntry = Entry(window, width=47, bg="black", fg="white")
textEntry.grid(row=2, column=0, sticky=W)
#Submit button
Button(window, text="Reverse", width=6, command=reverse, bg="black", fg="white").grid(ipadx=10, ipady=5)
#Output label
Label(window, text="The reversed string: ", bg="black", fg="white").grid(row=4, column=0, sticky=W)
#Output
output = Text(window, width=35, height=1, background="black")
output.grid(row=5, column=0, sticky=W)
#Exit button
Button(window, text="Exit", width=6, command=close_window, bg="black", fg="white").grid(ipadx=10, ipady=5)

window.mainloop()
