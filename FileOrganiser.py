import os
import shutil
import customtkinter

# used custontkinter for the GUI

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("File Organiser")
root.geometry("500x350")

def close_window(window):
    window.destroy()


def open_new_window(lable_text):
    new_window = customtkinter.CTk()
    new_window.title("Alert")
    new_window.geometry("300x150")
    new_frane = customtkinter.CTkFrame(master=new_window)
    new_frane.pack(pady=20, padx=60, fill="both", expand=True)
    lable = customtkinter.CTkLabel(master=new_frane, text=lable_text)
    lable.pack(pady=20, padx=10)
    button = customtkinter.CTkButton(master=new_frane, text="Okay", command=lambda: new_window.destroy())
    button.pack(pady=12, padx=10)
    new_window.mainloop()

def FileManage(path):
    try:
        files = os.listdir(path)
        for file in files:
            filename, file_extention = os.path.splitext(file)
            file_extention  = file_extention[1:]

            if os.path.exists(path+"/"+file_extention):
                shutil.move(path+"/"+file, path+"/"+file_extention+"/"+file)
            else:
                os.makedirs(path+"/"+file_extention)
                shutil.move(path+"/"+file, path+"/"+file_extention+"/"+file)
        open_new_window("Files have been sorted successfully")
    except Exception as e:
        open_new_window("Please provide a valid path")

frane = customtkinter.CTkFrame(master=root)
frane.pack(pady=20, padx=60, fill="both", expand=True)

lable = customtkinter.CTkLabel(master=frane, text="Enter the path of the directory to be sorted: ")
lable.pack(pady=20, padx=10)
lable.configure(font=("Arial", 18))

path_entry = customtkinter.CTkEntry(master=frane, placeholder_text="Enter the path of the directory to be sorted")
path_entry.pack(pady=20, padx=10)
path_entry.configure(width=300, height=30, font=("Arial", 14))

button = customtkinter.CTkButton(master=frane, text="Sort", command=lambda: FileManage(path_entry.get()))
button.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frane, text="Close", command=lambda: close_window(root))
button.pack(pady=12, padx=10)

root.mainloop()