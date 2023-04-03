from tkinter import Entry, Label, Button, Tk

def convert_miles_to_kilometer(value=0):
  miles_value = float(miles.get()) or value
  kilometer_value = round(miles_value * 1.609344, 2)
  calc_kilometer.config(text=kilometer_value)

window = Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=500)

calculate= Button(text="Calculate", command=convert_miles_to_kilometer)
miles = Entry()
label_miles = Label(text="Miles")
label_is_equal = Label(text="is equal to")
calc_kilometer = Label(text="0")
label_km = Label(text="Km")



miles.bind('<Return>', convert_miles_to_kilometer)


miles.grid(row=0, column=1)
label_miles.grid(row=0, column=2)
label_is_equal.grid(row=1, column=0)
calc_kilometer.grid(row=1, column=1)
label_km.grid(row=1, column=2)
calculate.grid(row=2, column=1)


window.mainloop()