from tkinter import *
from tkinter import filedialog as fd
from PIL import Image, ImageTk

accepted_types = ['png', 'jpg', 'bmp']

window = Tk()
window.title("Watermark Adder")
window.minsize(width=500, height=500)
window.config(padx=10, pady=10, bg="#f7f5dd")

heading = Label(text="Welcome to Watermark Adder", font=("Arial", 24, "bold"), fg='blue')
heading.grid(column=0, row=0, columnspan=2)

heading = Label(text="Example of watermark", font=("Arial", 12, "bold"), fg='black')
heading.grid(column=0, row=2)

instructions = Label(text="", font=("Arial", 10), fg='black')
instructions.grid(column=1, row=2)

canvas = Canvas(width=200, height=300, highlightthickness=0)
image = PhotoImage(file="silhouette.png")
image2 = image.subsample(13, 13)
canvas.create_image(100, 150, image=image2)
canvas.grid(column=0, row=3)


def press():
    image_path = fd.askopenfilename()
    print(image_path)
    if image_path.split('.')[1] not in accepted_types:
        instructions.config(text="Image filetype is not supported")
    else:
        image = Image.open(image_path)
        width, height = image.size
        image.show()
        watermark = Image.open('silhouette.png')
        watermark.thumbnail((int(width/2), int(height/2)))
        instructions.config(text="Image saved.")



upload = Button(command=press, text="Upload")
upload.grid(column=1, row=3)

window.mainloop()
