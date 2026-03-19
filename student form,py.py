from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Student Form")

# optional icon
try:
    root.iconbitmap("pixel2.ico")
except:
    pass

root.geometry('500x500+0+0')
root.configure(background='#00704A')

# image
img = Image.open('star.png')
resize_img = img.resize((100,70))
img = ImageTk.PhotoImage(resize_img)

img_label = Label(root, image=img, bg="#512E9C")
img_label.pack(pady=10, padx=20)

# title
text_label = Label(root, text="Giet Bucks",
font=('Arial',18,'bold'),
bg="#9CAA06",
fg='white')
text_label.pack(pady=10, padx=20)

# email
email_label = Label(root, text="Email",
font=('Arial',18,'bold'),
bg="#705000",
fg='white')
email_label.pack(pady=(20,5))

email_entry = Entry(root, font=('Arial',18,'bold'),
fg='white', bg='grey')
email_entry.pack(pady=(5,10))

# password
password_label = Label(root, text="Password",
font=('Arial',18,'bold'),
bg="#700065",
fg='white')
password_label.pack(pady=(20,5))

password_entry = Entry(root, font=('Arial',18,'bold'),
fg='white', bg='grey', show="*")
password_entry.pack(pady=(5,10))

# login button
login_btn = Button(root, text="Login",
font=('Arial',18,'bold'),
bg="#700016",
fg='white')
login_btn.pack(pady=(10,10))

root.mainloop()
