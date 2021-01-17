from tkinter import Tk, Label, Button, Entry, END


window = Tk()
window.title("Simple Calculator")


e = Entry(window, width=35,)
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def button_click(number):
    e.insert(END, number)

def button_c():
    a = e.get()
    b = a[:-1]
    e.delete(0, END)
    e.insert(END, b)

def button_clear():
    e.delete(0, END)

def button_operation(operation):
    e.insert(END, " " + operation + " ")

def button_equal():
    operasi = e.get()
    operasi.replace(" ", "")
    hasil = eval(operasi)
    e.insert(END, f" = {hasil}")

# membuat tombol
tombol1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
tombol2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
tombol3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
tombol4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
tombol5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
tombol6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
tombol7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
tombol8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
tombol9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
tombol0 = Button(window, text="0", padx=90, pady=20, command=lambda: button_click(0))

tombol_tambah = Button(window, text="+", padx=40, pady=10, command=lambda: button_operation("+"))
tombol_kurang = Button(window, text="-", padx=40, pady=10, command=lambda: button_operation("-"))
tombol_kali = Button(window, text="x", padx=40, pady=10, command=lambda: button_operation("*"))
tombol_bagi = Button(window, text=":", padx=40, pady=10, command=lambda: button_operation("/"))
tombol_hapus = Button(window, text="C", padx=40, pady=20, command=button_c)
tombol_clear = Button(window, text="AC", padx=40, pady=20, command=button_clear)
tombol_sama_dengan = Button(window, text="=", padx=40, pady=50, command=button_equal)

tombol_koma = Button(window, text=",", padx=40, pady=20, command=lambda: button_click("."))

# meletakkan tombol
tombol1.grid(row=4, column=0)
tombol2.grid(row=4, column=1)
tombol3.grid(row=4, column=2)

tombol4.grid(row=3, column=0)
tombol5.grid(row=3, column=1)
tombol6.grid(row=3, column=2)

tombol7.grid(row=2, column=0)
tombol8.grid(row=2, column=1)
tombol9.grid(row=2, column=2)

tombol0.grid(row=5, column=0, columnspan=2)
tombol_tambah.grid(row=1, column=0)
tombol_kurang.grid(row=1, column=1)
tombol_kali.grid(row=1, column=2)
tombol_bagi.grid(row=1, column=3)

tombol_hapus.grid(row=2, column=3)
tombol_clear.grid(row=3, column=3)
tombol_sama_dengan.grid(row=4, column=3, rowspan=2)
tombol_koma.grid(row=5, column=2)


window.mainloop()
