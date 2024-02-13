from tkinter import *


def calculated_answer():
    new_num = float(entry.get())
    km = round(new_num * 1.609)
    answer.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=10, pady=10)

mile_label = Label(text="Miles", font=("Arial", 10))
mile_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=10, pady=10)

answer = Label(text="0")
answer.grid(column=1, row=1)

calculate_button = Button(text="Calculate", command=calculated_answer)
calculate_button.grid(column=1, row=2)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

entry = Entry(width=10)
entry.insert(END, "0")
entry.grid(column=1, row=0)

window.mainloop()
