#import the tkinter library
import tkinter as tk
from tkinter import messagebox

#function to retrieve the data from the GUI and display it in a messagebox
def submit():
    forename = ent1.get()
    surname = ent2.get()
    age = ent3.get()
    funfact = txt1.get("1.0", "end")

    tk.messagebox.showinfo(title="Your Information", message=
                                "Your full name is: " + forename + " " + surname + "\n"
                                "Your age is: " + age + "\n"
                                "A fun fact about you is: " + funfact)

window = tk.Tk()

#GUI widgets
lbl1 = tk.Label(text="Forename:")
lbl2 = tk.Label(text="Surname:")
lbl3 = tk.Label(text="Age:")
lbl4 = tk.Label(text="A Fun Fact About You:")

ent1 = tk.Entry()
ent2 = tk.Entry()
ent3 = tk.Entry()
txt1 = tk.Text(width=50, height=5)

#GUI grid to contain and organise widgets
lbl1.grid(row=0, column=0, padx=5, pady=5)
lbl2.grid(row=1, column=0, padx=5, pady=5)
lbl3.grid(row=2, column=0, padx=5, pady=5)
lbl4.grid(row=3, column=0, padx=5, pady=5)

ent1.grid(row=0, column=1, padx=5, pady=5)
ent2.grid(row=1, column=1, padx=5, pady=5)
ent3.grid(row=2, column=1, padx=5, pady=5)
txt1.grid(row=3, column=1, padx=5, pady=5)

#Submit Button
submitBtn = tk.Button(text="Submit", command=submit)
submitBtn.grid(row=5, columnspan=2)

window.mainloop()
