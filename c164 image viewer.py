from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

root.title("Image Viewer")
root.geometry("500x500")
root.configure(background = "MediumPurple1")

label = Label(root, bg = "MediumPurple1", highlightthickness=5)
label.place(relx = 0.5, rely = 0.1, anchor = CENTER)

img_path = " "
def openImage() :
    global img_path
    img_path = filedialog.askopenfilename(title  = "Open Text File",
                                          filetypes =[( "Image Files", 
                                          "*.jpg;,*.gif;*.jpg;;*.png;*txt")])
    print(img_path)
    img = ImageTk.PhotoImage(Image.open("koala.jpg"))
    label["image"] = img
    img.close()
    
open_img_button = Button(root, ("Times New Roman", 10, "bold"), bg = "cyan", fg = "black", relief = SOLID, padx = 10, pady = 10, command = openImage)
    
    
root.mainloop()