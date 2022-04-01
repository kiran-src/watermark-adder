from tkinter import *
from PIL import Image, ImageTk

window = Tk()
window.title("Watermark Adder")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10, bg="#f7f5dd")

heading = Label(text="Welcome to Watermark Adder", font=("Arial", 24, "bold"), fg='blue')
heading.grid(column=0, row=0, columnspan=2)

heading = Label(text="Example of watermark", font=("Arial", 12, "bold"), fg='black')
heading.grid(column=0, row=2)

canvas = Canvas(width=200, height=300, highlightthickness=0)
image = PhotoImage(file="silhouette.png")
image2 = image.subsample(13, 13)
canvas.create_image(100, 150, image=image2)
canvas.grid(column=0, row=3)


def press():
    pass


upload = Button(command=press, text="Upload")
upload.grid(column=1, row=3)

window.mainloop()
