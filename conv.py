from tkinter import *
from tkinter import font
from tkinter import filedialog
from tkinter.filedialog import askopenfilenames
import img2pdf

root = Tk()
root.geometry('400x200')
root.title("Converter")

def pilih():
    global file_names
    file_names = askopenfilenames(initialdir="/" , title="pilih gambar")

def konvert():
    hasil = filedialog.asksaveasfilename(defaultextension='.pdf')
    with open(hasil, "wb") as f:
        f.write(img2pdf.convert(file_names))

Label(root, text = "Converter Image to PDF\n By : Rifal Kurniawan", font = "italic 15 bold", bg="yellow").pack(pady=10)

Button(root, text="Pilih Gambar", relief= "solid" , command = pilih , font=14, bg="blue").pack(pady=10)
Button(root, text="Convert to PDF", relief="solid", command=konvert, bg="red", font=15).pack(pady=10)

root.mainloop()