from tkinter import *


def convert_miles_to_km():
    miles = float(miles_input.get())
    km = round(miles * 1.6, 1)
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=350, height=200)
window.config(padx=20, pady=30)


is_equal_to_label = Label(text="is equal to", font=("Arial", 15))
is_equal_to_label.grid(column=0, row=1)
is_equal_to_label.config(padx=20, pady=20)

km_result_label = Label(text="0", font=("Arial", 15))
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=20, pady=20)

km_label = Label(text="Km", font=("Arial", 15))
km_label.grid(column=2, row=1)
km_label.config(padx=20, pady=20)

miles_label = Label(text="miles", font=("Arial", 15))
miles_label.grid(column=2, row=0)

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

calculate_button = Button(text="calculate", command=convert_miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()
