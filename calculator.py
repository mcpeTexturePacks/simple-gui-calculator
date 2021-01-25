#!/usr/bin/python3
from tkinter import Tk, Label, Button, Entry, END


window = Tk()
window.title("Simple Calculator by Hasban")
window.configure(background = "gray")

e = Entry(window, width=35, font=("Arial", 15))
e.grid(row=0, column=0, columnspan=5, padx=10, pady=10)


def tombol_klik(angka):
    e.insert(END, angka)

def tombol_del():
    a = e.get()
    try:
        if " " in a[-2]:
	    b = a[:-2]
        else:
            b = a[:-1]
    except:
	b = a[:-1]
    e.delete(0, END)
    e.insert(END, b)

def tombol_DA():
    e.delete(0, END)

def tombol_operasi(operasi):
    if operasi == "-" and str(e.get()) == "":
        e.insert(END, operasi)
    else:
        e.insert(END, " " + operasi + " ")

def tombol_sama_dengan():
    operasi = e.get()
    operasi.replace(" ", "")
    try:
        hasil = eval(operasi)
        e.insert(END, f" = {hasil}")
    except:
        operasi.replace("=", "")
        hasil = eval(operasi)
        e.insert(END, f" = {hasil}")

def tombol_lanjut():
    operasi = e.get()
    


# membuat tombol
tombol1 = Button(window, text="1", padx=40, pady=20, command=lambda: tombol_klik(1))
tombol2 = Button(window, text="2", padx=40, pady=20, command=lambda: tombol_klik(2))
tombol3 = Button(window, text="3", padx=40, pady=20, command=lambda: tombol_klik(3))
tombol4 = Button(window, text="4", padx=40, pady=20, command=lambda: tombol_klik(4))
tombol5 = Button(window, text="5", padx=40, pady=20, command=lambda: tombol_klik(5))
tombol6 = Button(window, text="6", padx=40, pady=20, command=lambda: tombol_klik(6))
tombol7 = Button(window, text="7", padx=40, pady=20, command=lambda: tombol_klik(7))
tombol8 = Button(window, text="8", padx=40, pady=20, command=lambda: tombol_klik(8))
tombol9 = Button(window, text="9", padx=40, pady=20, command=lambda: tombol_klik(9))
tombol0 = Button(window, text="0", padx=90, pady=20, command=lambda: tombol_klik(0))
tombol_koma = Button(window, text=",", padx=43, pady=20, command=lambda: tombol_klik("."))

tombol_tambah = Button(window, text="+", padx=39, pady=10, command=lambda: tombol_operasi("+"))
tombol_kurang = Button(window, text="-", padx=42, pady=10, command=lambda: tombol_operasi("-"))
tombol_kali = Button(window, text="x", padx=40, pady=10, command=lambda: tombol_operasi("*"))
tombol_bagi = Button(window, text=":", padx=43, pady=10, command=lambda: tombol_operasi("/"))
tombol_hapus = Button(window, text="del", padx=35, pady=20, command=tombol_del)
tombol_clear = Button(window, text="DA", padx=36, pady=20, command=tombol_DA)
tombol_sama_dengan = Button(window, text="=", padx=40, pady=50, command=tombol_sama_dengan)


# meletakkan tombol
tombol1.grid(row=5, column=0)
tombol2.grid(row=5, column=1)
tombol3.grid(row=5, column=2)

tombol4.grid(row=4, column=0)
tombol5.grid(row=4, column=1)
tombol6.grid(row=4, column=2)

tombol7.grid(row=3, column=0)
tombol8.grid(row=3, column=1)
tombol9.grid(row=3, column=2)

tombol0.grid(row=6, column=0, columnspan=2)
tombol_tambah.grid(row=2, column=0)
tombol_kurang.grid(row=2, column=1)
tombol_kali.grid(row=2, column=2)
tombol_bagi.grid(row=2, column=3)

tombol_hapus.grid(row=3, column=3)
tombol_clear.grid(row=4, column=3)
tombol_sama_dengan.grid(row=5, column=3, rowspan=2)
tombol_koma.grid(row=6, column=2)


window.mainloop()
