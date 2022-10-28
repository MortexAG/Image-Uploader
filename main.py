import requests
import os
import PIL
import dotenv
from dotenv import load_dotenv
import tkinter as tk
from tkinter import NW, Button, Canvas, Frame, Label, Listbox, PhotoImage, Tk, Toplevel, messagebox, ttk
from tkinter import filedialog as fd
from PIL import ImageTk, Image
load_dotenv()

clientid = os.environ["clientid"]
clientsecret = os.environ["clientsecret"]
accesstoken = os.environ["accesstoken"]

# The Image Choice Button


def main_app():
    # Main App Frame
    root =tk.Tk()
    root.title("Image Uploader")
    root.geometry("500x500")
    root.resizable(True, True)

    def start_upload():
        image_link = upload_image(filename)
        uploaded_link = Listbox(root, height = 5, width = 30, bg = "white", activestyle = 'dotbox', font = "Helvetica", fg = "Black")
        uploaded_link.insert(1, image_link)
        uploaded_link.pack(expand=True)
        messagebox.showinfo(title="Upload Successful", message="The Image Link is\n"+image_link)
        return image_link
    def upload_button():
        upload_button = ttk.Button(
        root,
        text='Upload The Image',
        command=start_upload
    )
        upload_button.pack(expand=True)


    def selected_image():
        image_window = Toplevel(root)
        image_window.geometry("700x700")
        image_window.title(filename)
        
        ## Show The Displayed Image  
        # Create an object of tkinter ImageTk
        global image_var
        image_var = ImageTk.PhotoImage(Image.open(filename))

        # Create a Label Widget to display the text or Image
        Label(image_window, image=image_var).pack()
        upload_button()
    def select_file(): 
        filetypes = (
        ('All files', '*.*'),
        ('All files', '*.*')
        )
        global filename
        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes)
        print(filename)
        selected_image()
        #upload_image(filename)
        

    # open button
    open_button = ttk.Button(
        root,
        text='Open a File',
        command=select_file
    )

    open_button.pack(expand=True)

    def upload_image(imagepath):
        url = "https://api.imgur.com/3/upload"

        payload={}
        files=[
        ('image',('file',open(f'{imagepath}','rb'),'application/octet-stream'))
        ]
        headers = {
          'Authorization': f'Bearer {accesstoken}'
        }

        response = requests.request("POST", url, headers=headers, data=payload, files=files)
        result = response.json()
        print(result)
        print(result["data"]["link"])
        return result["data"]["link"]
    def get_image(image_id):
        url = f"https://api.imgur.com/3/image/{image_id}"

        payload={}
        headers = {
          'Authorization': f'Client-ID {clientid}'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        result = response.json()
        print(result)
    #get_image('')
    #upload_image("test-image.png", "test-image.png")
    root.mainloop()
main_app()