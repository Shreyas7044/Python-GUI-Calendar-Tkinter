# Importing tkinter module
from tkinter import *

# Importing calendar module
import calendar

# Function to show calendar of the given year
def showCalendar():
    gui = Tk()
    gui.config(background='grey')
    gui.title("Calendar for the Year")
    gui.geometry("550x600")

    year = int(year_field.get())
    gui_content = calendar.calendar(year)

    calYear = Label(gui, text=gui_content, font="Consolas 10 bold", justify=LEFT)
    calYear.pack(padx=20, pady=20)

    gui.mainloop()

# Driver code
if __name__ == '__main__':
    new = Tk()
    new.config(background='grey')
    new.title("Calendar")
    new.geometry("250x180")

    cal = Label(new, text="Calendar", bg='grey', font=("Times", 28, "bold"))
    year = Label(new, text="Enter Year", bg='grey')
    year_field = Entry(new)
    button = Button(new, text='Show Calendar', fg='black', bg='blue', command=showCalendar)

    cal.pack(pady=5)
    year.pack()
    year_field.pack()
    button.pack(pady=10)

    new.mainloop()